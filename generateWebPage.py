
# Uses template.html as a template, and replaces some text in it to make a new web page.
# for a language.
import sys


def generateWebPage(dirName):
    orthographyName = open(dirName + '/name.txt').read()
    titled = sys.stdin.read().replace('ISO-233 Arabic Romanization Template', orthographyName)
    replacements = open(dirName + '/replacements.txt').read()
    print(titled.replace('[[\'11\', \'2\']]', replacements))

 
def generateWebPageAndSave(dirName, templateFileContents):
    orthographyName = open(dirName + '/name.txt').read()
    titled = templateFileContents.replace('ISO-233 Arabic Romanization Template', orthographyName)
    replacements = open(dirName + '/replacements.txt').read()
    return titled.replace('[[\'11\', \'2\']]', replacements)

if __name__ == "__main__":
    dirName = sys.argv[1] # 1st argument: should be name of directory in the current directory
    generateWebPage(dirName)