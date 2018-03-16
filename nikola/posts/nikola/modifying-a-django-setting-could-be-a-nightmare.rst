.. title: Modifying a Django setting could be a nightmare
.. slug: modifying-a-django-setting-could-be-a-nightmare
.. date: 2018-03-15 22:55:53 UTC-03:00
.. tags: django, read the docs, python, cuenca, ecuador
.. category:
.. link:
.. description:
.. type: text

I've been working at Read *the* Docs for four months more or less at
this time. Although I've been using Django for a decade now, there are
many things that I never used, forget or don't know how they work
internally.

During the last three or four weeks I worked in a new feature for the
corporate site of Read the Docs (https://readthedocs.com/) and I had a
lot of different problems: mainly because I didn't know the full
codebase, but also because I never used some pieces of technology
involved to make this feature.

So, what do you do when you are afraid of breaking everything? You
write many test to cover your ass! That's what I did and I felt very
comfortable when I started writing the logic of the feature
itself --of course, to write the tests I had to ask many questions to
my team to be sure the tests were accurate regarding what they were
testing.

Finally, the PR was tested for some members of the team, everything
worked as expected, the code was merged and deployed. Successful
story, right?

One of two days later, I started seeing one of my tests related to that
PR failing locally. I did a simple PR to run the test in CircleCI and
it also failed there. "WTF? This doesn't make sense" -I thought. I did
the manual QA locally and the code worked as expected but the test
were failing but... It didn't make sense because the initial tests
under CircleCI before merging the PR were passing and now *without any
change at all* this specific test wasn't passing. I was very
confused.

.. TEASER_END

I went to the code of my tests to find something strange and after
taking a look at this code I didn't find anything that called my
attention directly but I found that I was mixing `@override_settings`
and `@modify_settings` as decorators of the class. "That may be a
reason... Really? Why?" -I was confused. I went to the documentation,
search at Google to see if the first results could give some clue and
after a couple of hours reading, thinking and shouting alone I
realized that I was using *both* options of the `@modify_settings
<https://docs.djangoproject.com/en/1.9/topics/testing/tools/#django.test.SimpleTestCase.modify_settings>`_
decorator: `append` **and** `remove` which, in theory, is not a
problem.


.. note::

   What is the difference between `@override_settings` and
   `@modify_settings`? Well, one allows you to replace the setting
   completely and the other one allows you to append, prepend or
   remove values from the current value of the setting.

As I wanted to modify the `MIDDLEWARE_CLASSES` to inject a new one *in
the middle* of the others, I needed to *remove* the ones that go
*after* the one I wanted to inject and then add mine (the new one)
plus the ones that I had removed. Am I right?

.. epigraph::

   I'm sure that at this point I'm wrong and there should be a much
   better way of doing this, but I'm already writing the post :)

So, my code looks something like:

.. code:: python

   @modify_settings(MIDDLEWARE_CLASSES={
       'append': [
           'readthedocsinc.middleware.MyOwnMiddleware',
           'externallib.middleware.ExternalMiddleware',
       ],
       'remove': [
           'externallib.middleware.NoNeededMiddleware',
           'externallib.middleware.ExternalMiddleware',
       ],
   })
   class FooBar(TestCase):
       # ...

In my case, `NoNeededMiddleware` wasn't needed for the tests and it
had to be completely removed. `ExternalMiddleware` was needed but
`MyOwnMiddleware` should precede it; that's why I needed to first
remove it and then append it -in another position in the list, though.

Anything wrong up to here? No. Well, yes. Oh... "No, the test are
passing", or in a better way "The tests were passing right before the
deploy but now there is one that it's not passing anymore"

At this point, I did what I learnt from my first boss in my
professional career: I went to the `Django source code of
@modify_settings
<https://github.com/django/django/blob/2.0.3/django/test/utils.py#L471-L482>`_
and I found the issue: it removes everything from `remove` key and
appends everything from `append` key. Makes sense.

Now, which operation is executed first? AHA! Well, it depends since
dictionaries don't have order (< Python 3.6), sometimes it could be
`remove` and sometimes it could be `append`. So, I'd say that all the
planets were aligned to pass all the tests locally and in CircleCI
*before* merging, and after merging they got unaligned and the order
started behaving in the other way :)

What I did? I just used `collections.OrderedDict` and put `remove` as
the first element in the dictionary, and then `append`. That way, I'm
100% sure that first I'm removing the middlewares I don't need and
then I'm adding the ones that I'm interested in the proper order.

The final code looks like this:

.. code:: python

   from collections import OrderedDict
   @modify_settings(MIDDLEWARE_CLASSES=OrderedDict([
       (
           'remove',
           [
               'externallib.middleware.NoNeededMiddleware',
               'externallib.middleware.ExternalMiddleware',
           ],
       ).
       (
           'append',
           [
               'readthedocsinc.middleware.MyOwnMiddleware',
               'externallib.middleware.ExternalMiddleware',
           ],
       ),
   ]))
   class FooBar(TestCase):
       # ...


I think this should be clearly detailed in the Django documentation of
`@modify_settings` since the behaviour is way different and can cause
a lot of time lost because of this --even worse if you are working
with Python 2 which will randomly do one or the other first.
