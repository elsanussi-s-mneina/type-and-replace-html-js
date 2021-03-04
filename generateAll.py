
# Uses template.html as a template, and replaces some text in it to make a new web page.
# for a language.
import sys

from generateWebPage import generateWebPageAndSave

_templateFileName = "template.html"

def getHTMLPageName(directory):
    return directory + "QuickTypist.html"

def generateIndexPage(directories):
    fileContents = ""
    for directory in directories:
        fileContents += "<li><a href='" + getHTMLPageName(directory) +"'>" + directory + "</a></li>\n"

    open("index.html", "w").write(fileContents)

def generateWebPages(directories):

    templateContents = open(_templateFileName,'r').read()

    for directory in directories:
        genFileContents = generateWebPageAndSave(directory, templateContents)
        open(getHTMLPageName(directory), 'w').write(genFileContents)
    generateIndexPage(directories)



if __name__ == "__main__":
    directories = ["berber-latin-alphabet","french","german","icelandic","irish","iso233","latin","maltese","mehri-soqotri","pinyin","polish","qamus-buckwalter","qamus-buckwalter-inverse","scottish-gaelic","spanish"]
    
    generateWebPages(directories)