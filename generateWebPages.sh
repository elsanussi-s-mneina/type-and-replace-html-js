
# Uses template.html as a template, and replaces some text in it to make a new web page.
# for each language.

python3 -c "import sys; orthographyName = open('iso233/name.txt').read(); titled = sys.stdin.read().replace('ISO-233 Arabic Romanization Template', orthographyName); replacements = open('iso233/replacements.txt').read(); print(titled.replace('[[\'11\', \'2\']]', replacements));" < ./template.html > ./iso233QuickTypist.html
python3 -c "import sys; orthographyName = open('berber-latin-alphabet/name.txt').read(); titled = sys.stdin.read().replace('ISO-233 Arabic Romanization Template', orthographyName); replacements = open('berber-latin-alphabet/replacements.txt').read(); print(titled.replace('[[\'11\', \'2\']]', replacements));" < ./template.html > ./berber-latin-alphabetQuickTypist.html
python3 -c "import sys; orthographyName = open('french/name.txt').read(); titled = sys.stdin.read().replace('ISO-233 Arabic Romanization Template', orthographyName); replacements = open('french/replacements.txt').read(); print(titled.replace('[[\'11\', \'2\']]', replacements));" < ./template.html > ./frenchQuickTypist.html
python3 -c "import sys; orthographyName = open('spanish/name.txt').read(); titled = sys.stdin.read().replace('ISO-233 Arabic Romanization Template', orthographyName); replacements = open('spanish/replacements.txt').read(); print(titled.replace('[[\'11\', \'2\']]', replacements));" < ./template.html > ./spanishQuickTypist.html
python3 -c "import sys; orthographyName = open('maltese/name.txt').read(); titled = sys.stdin.read().replace('ISO-233 Arabic Romanization Template', orthographyName); replacements = open('maltese/replacements.txt').read(); print(titled.replace('[[\'11\', \'2\']]', replacements));" < ./template.html > ./malteseQuickTypist.html

