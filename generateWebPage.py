
# Uses template.html as a template, and replaces some text in it to make a new web page.
# for a language.

def generateWebPageAndSave(dirName, templateFileContents):
    orthographyName = open(dirName + '/name.txt').read()
    titled = templateFileContents.replace('ISO-233 Arabic Romanization Template', orthographyName)
    replacements = open(dirName + '/replacements.txt').read()
    return titled.replace('[[\'11\', \'2\']]', replacements)
