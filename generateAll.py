
# Uses template.html as a template, and replaces some text in it to make a new web page.
# for a language.
import sys
from typing import List
from generateWebPage import generateWebPageAndSave

_typeAndReplaceTemplateFileName: str = "type_and_replace_template.html"
_typeAndClickTemplateFileName: str = "type_and_click_template.html"
_generatedPath = "generated/"

def getTypeAndReplaceHTMLPageName(language: str):
    return language + "QuickTypist.html"

def getTypeAndClickHTMLPageName(language: str):
    return language + "ClickTypist.html"

def getTypeAndReplaceHTMLPagePath(language: str):
    return _generatedPath + getTypeAndReplaceHTMLPageName(language)

def getTypeAndClickHTMLPagePath(language: str):
    return _generatedPath + getTypeAndClickHTMLPageName(language)


def generateIndexPage(directories: List[str]):
    fileContents = ""
    for directory in directories:
        fileContents += "<li><a href='" + getTypeAndReplaceHTMLPageName(directory) +"'>" + directory + "(quick)</a></li>\n"
        fileContents += "<li><a href='" + getTypeAndClickHTMLPageName(directory) +"'>" + directory + " (simple)</a></li>\n"

    open(_generatedPath + "index.html", "w").write(fileContents)


def generateWebPages(directories: List[str]):
    generateTypeAndReplaceWebPages(directories)
    generateTypeAndClickWebPages(directories)
    generateIndexPage(directories)


def generateTypeAndReplaceWebPages(directories):
    templateContents = open(_typeAndReplaceTemplateFileName, 'r').read()

    for directory in directories:
        genFileContents = generateWebPageAndSave(directory, templateContents)
        open(getTypeAndReplaceHTMLPagePath(directory), 'w').write(genFileContents)


def generateTypeAndClickWebPages(directories):
    templateContents = open(_typeAndClickTemplateFileName, 'r').read()

    for directory in directories:
        genFileContents = generateWebPageAndSave(directory, templateContents)
        open(getTypeAndClickHTMLPagePath(directory), 'w').write(genFileContents)


if __name__ == "__main__":
    directories = ["berber-latin-alphabet","french","german","icelandic","irish","iso233","latin","maltese","mehri-soqotri","pinyin","polish","qamus-buckwalter","qamus-buckwalter-inverse","scottish-gaelic","spanish", "portuguese"]
    
    generateWebPages(directories)
