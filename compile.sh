# This script updates the pdfs for different text files.
# You need pandoc for this to work, and also a unix shell.


# Compile classes doc. Change this to add more classes
cd character_creation/classes/
cat gunsmith.md > classes.md
cat alchemist.md >> classes.md
cat psion.md >> classes.md
cat warrior.md >> classes.md
cat runesmith.md >> classes.md
cat scientist.md >> classes.md
cat priest.md >> classes.md
cat thief.md >> classes.md
cat commoner.md >> classes.md
cat colossus.md >> classes.md
cat lycanthrope.md >> classes.md
sed -i 's/(└|┌|┐|┘|┬|▼)/+/g' classes.md
pandoc classes.md -o ../../pdf/classes.pdf
rm classes.md


# Compile supplements
cd ..
pandoc 3d4_body_types.md -o ../pdf/body_types.pdf
pandoc cultures_volume_1.md -o ../pdf/cultures.pdf
pandoc spell_compendium.md -o ../pdf/spells.pdf

# Compile basic edition
cd ..
pandoc basic_edition.md -o pdf/basic_edition.pdf