set -e
for x in `ls *.wp`; do pandoc --from=html --to=rst --normalize --output=migrated/`basename $x .wp`.rst $x;done
