#!/bin/sh

if [ -n "$1" ]; then
    FILES_TO_CONVERT="$@"
else
    FILES_TO_CONVERT="$(find . -name '*.rst')"
fi

for f in $FILES_TO_CONVERT; do
    perl -i -0 \
    -pe "s/\|image(\d\d?)\|. /\|image\1\|\n\n/g;" \
    -pe "s/\|image(\d\d?)\| /\|image\1\|\n\n/g;" \
    $f
done
