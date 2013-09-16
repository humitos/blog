set -e
for x in `ls *.wp`;
do pandoc \
    --from=html \
    --to=rst \
    --normalize \
    --reference-links \
    --output=migrated/$(basename $x .wp).rst \
    --template=/home/humitos/blog/nikola/utils/pandoc_template.rst \
    --variable="title:$(cat $(basename $x .wp).meta | head -n 1 | tail -n 1)" \
    --variable="slug:$(cat $(basename $x .wp).meta | head -n 2 | tail -n 1)" \
    --variable="date:$(cat $(basename $x .wp).meta | head -n 3 | tail -n 1)" \
    --variable="tags:$(cat $(basename $x .wp).meta | head -n 4 | tail -n 1)" \
    $x;
done
