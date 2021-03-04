
# Replaces some text in it to make a new web page.
# for a language.
import sys
from typing import List
from generateWebPage import fillTemplate

# You will need to modify the following line if you add or remove a language (directory).
_languageDirectories: List[str] = ["berber-latin-alphabet","french","german","icelandic","irish","iso233","latin","maltese","mehri-soqotri","pinyin","polish","qamus-buckwalter","qamus-buckwalter-inverse","scottish-gaelic","spanish", "portuguese"]


_typeAndReplaceTemplatePath: str = "type_and_replace_template.html"
_typeAndClickTemplatePath: str = "type_and_click_template.html"
_generatedPath: str = "generated/"

def typeAndReplaceFileName(language: str) -> str:
    """
    The name of the file where the Type
    and replace web application should be saved.
    """
    return language + "QuickTypist.html"

def typeAndClickFileName(language: str) -> str:
    """
    The name of the file where the Type and
    Click web application should be saved
    """
    return language + "ClickTypist.html"

def typeAndReplacePath(language: str) -> str:
    """
    The place where the Type and Replace page
    should be saved in this repository.
    """
    return _generatedPath + typeAndReplaceFileName(language)

def typeAndClickPath(language: str) -> str:
    """ The place where the Type and Click page
    should be saved in this repository
    """
    return _generatedPath + typeAndClickFileName(language)


def generateIndexPage(directories: List[str]) -> str:
    """
    Generates a page with a link to all the other generated pages.
    It only generates the contents of the body.
    """
    fileContents: str = ""
    for directory in directories:
        fileContents += "<li><a href='" + typeAndReplaceFileName(directory) +"'>" + directory + "(quick)</a></li>\n"
        fileContents += "<li><a href='" + typeAndClickFileName(directory) +"'>" + directory + " (simple)</a></li>\n"

    open(_generatedPath + "index.html", "w").write(fileContents)


def generateAll(directories: List[str]) -> None:
    """
    Generate the single page web app pages,
    and an index page.
    """
    generateTypeAndReplaceWebPages(directories)
    generateTypeAndClickWebPages(directories)
    generateIndexPage(directories)


def generateTypeAndReplaceWebPages(directories) -> None:
    """
    Generate web pages where the user types text,
    and some of it is replaced as they type,
    or after they press a button.
    """
    templateContents = open(_typeAndReplaceTemplatePath, 'r').read()

    for directory in directories:
        genFileContents = fillTemplate(directory, templateContents)
        open(typeAndReplacePath(directory), 'w').write(genFileContents)


def generateTypeAndClickWebPages(directories) -> None:
    """
    Generates web pages where the user types text,
    and for characters that do not exist on their
    keyboard (such as C with a cedilla),
    the user can click on a button near the
    text area.
    """
    templateContents = open(_typeAndClickTemplatePath, 'r').read()

    for directory in directories:
        genFileContents = fillTemplate(directory, templateContents)
        open(typeAndClickPath(directory), 'w').write(genFileContents)


# The following runs if this module is run as the main module:
if __name__ == "__main__":
    generateAll(_languageDirectories)
