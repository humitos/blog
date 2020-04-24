.. title: pytest.el custom runner
.. slug: pytest-el-custom-runner
.. date: 2020-04-24 17:51:18 UTC-03:00
.. tags: emacs, pytest, test, spacemacs
.. category:
.. link:
.. description:
.. type: text


pytest.el custom runner
=======================

I started using Spacemacs_ some weeks ago, and there is not too much more to add
than what I wrote in the README_ of my Emacs' configuration

.. _Spacemacs: https://spacemacs.org/
.. _README: https://github.com/humitos/emacs-configuration

.. epigraph::

   I used to have a very customized Emacs configuration with lot of packages, hotkeys, custom variables and a lot of things.
   Then, one day, I met Spacemacs. Basically, it is exactly what I had but better and maintained by other people.

   -- me

We have a very custom way to run tests:

- use a specific virtualenv
- we run the test inside docker
- we use a docker-compose wrapper made with invoke_
- we use tox_ to run pytest
- filepath of test file in host does not exist in the container
- etc

.. _invoke: http://docs.pyinvoke.org/
.. _tox: https://tox.readthedocs.io/


Basically, we need a very specific command to run the test and, of course that `pytest.el`_ won't know what to do here,
and it will fail even trying to guess hard. So, I needed a way to customize what is the command that pytest.el is going to execute.
Fortunately, the author already thought on some variables that helped me to make me happy -but there is one function that can't be
replaced using a customizable variable. I had to *override* it.

.. _pytest.el: https://github.com/ionrock/pytest-el

#. Define the variables I need in ``.dir-locals.el``, so it only affects the project I want

   .. code-block:: lisp

      ((python-mode
        (pytest-cmd-flags . "-x")
        (pytest-global-name . "~/.pyenv/versions/readthedocs.org/bin/inv docker.test -a")
        (pytest-cmd-format-string . "cd '%s' && %s '-e py36 -- %s %s'")
        (pytest-remove-path . "/home/humitos/rtfd/code/readthedocs.org/readthedocs/")))  ;; Extra variable added by myself

#. Override pytest.el ``pytest-cmd-format`` function

   .. code-block:: lisp

      ;; .emacs.d/private/local/docker-tox-pytest.el
      (defcustom pytest-remove-path ""
        "Path to remove from pytest test-names variable")

      (with-eval-after-load 'pytest
        (defun pytest-cmd-format (format-string working-directory test-runner command-flags test-names)
          "Override default function to remove local path."
          (format format-string working-directory test-runner command-flags (replace-regexp-in-string pytest-remove-path "" test-names)))
        )

#. Load my ``docker-tox-pytest.el`` file from Spacemacs

   .. code-block:: lisp

      (load "~/.emacs.d/private/local/docker-tox-pytest.el")


That's all!

Now a simple ``SPC m t t`` somewhere in the function that I want to test will call the command I need and will execute **only** that test.
