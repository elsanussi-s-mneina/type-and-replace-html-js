
# Uses template.html as a template, and replaces some text in it to make a new web page.
# for a language.
import sys
from typing import List
from generateWebPage import generateWebPageAndSave

_typeAndReplaceTemplateFileName: str = "template.html"
_typeAndClickTemplateFileName: str = "type_and_click_template.html"

def getTypeAndReplaceHTMLPageName(directory: str):
    return directory + "QuickTypist.html"

def getTypeAndClickHTMLPageName(directory: str):
    return directory + "ClickTypist.html"

def generateIndexPage(directories: List[str]):
    fileContents = ""
    for directory in directories:
        fileContents += "<li><a href='" + getTypeAndReplaceHTMLPageName(directory) +"'>" + directory + "(quick)</a></li>\n"
        fileContents += "<li><a href='" + getTypeAndClickHTMLPageName(directory) +"'>" + directory + " (simple)</a></li>\n"

    open("index.html", "w").write(fileContents)


def generateWebPages(directories: List[str]):
    generateTypeAndReplaceWebPages(directories)
    generateTypeAndClickWebPages(directories)
    generateIndexPage(directories)


def generateTypeAndReplaceWebPages(directories):
    templateContents = open(_typeAndReplaceTemplateFileName, 'r').read()

    for directory in directories:
        genFileContents = generateWebPageAndSave(directory, templateContents)
        open(getTypeAndReplaceHTMLPageName(directory), 'w').write(genFileContents)


def generateTypeAndClickWebPages(directories):
    templateContents = open(_typeAndClickTemplateFileName, 'r').read()

    for directory in directories:
        genFileContents = generateWebPageAndSave(directory, templateContents)
        open(getTypeAndClickHTMLPageName(directory), 'w').write(genFileContents)


if __name__ == "__main__":
    directories = ["berber-latin-alphabet","french","german","icelandic","irish","iso233","latin","maltese","mehri-soqotri","pinyin","polish","qamus-buckwalter","qamus-buckwalter-inverse","scottish-gaelic","spanish", "portuguese"]
    
    generateWebPages(directories)