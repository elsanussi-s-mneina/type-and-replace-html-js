
# Replaces some text in it to make a new web page.
# for a language.
import sys
import os
from typing import List
from generateWebPage import fillTemplate

# You will need to modify the following line if you add or remove a language (directory).
_languageDirectories: List[str] = ["berber-latin-alphabet","french","german","icelandic","irish","iso233","latin","maltese","mehri-soqotri","pinyin","polish","scottish-gaelic","spanish", "portuguese", "experiment1", "experiment2", "experiment3"]

# The following is for situations where it does not make sense to have
# the type-and-click application generated. This may be useful for transliteration systems
# that use ASCII characters for one of their sides.
_languagesTypeAndReplaceOnly : List[str] = ["qamus-buckwalter","qamus-buckwalter-inverse"]

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
        fileContents += "<li><a href='" + typeAndReplaceFileName(directory) +"'>" + directory + " (Type and Replace)</a></li>\n"
        if (directory not in _languagesTypeAndReplaceOnly):
            fileContents += "<li><a href='" + typeAndClickFileName(directory) +"'>" + directory + " (Type and Click)</a></li>\n"

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

    scriptPath = _typeAndReplaceTemplatePath.replace('_template.html', ".js")
    scriptContents = open(scriptPath, 'r').read()
    
    for directory in directories:
        genFileContents = fillTemplate(directory, templateContents, scriptContents)
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

    scriptPath = _typeAndClickTemplatePath.replace('_template.html', ".js")
    scriptContents = open(scriptPath, 'r').read()

    for directory in directories:
        genFileContents = fillTemplate(directory, templateContents, scriptContents)
        open(typeAndClickPath(directory), 'w').write(genFileContents)


# The following runs if this module is run as the main module:
if __name__ == "__main__":
    # Generate all of them
    generateAll(_languageDirectories + _languagesTypeAndReplaceOnly)

    # but remove those that should not have a type and click app after the fact.
    for directory in _languagesTypeAndReplaceOnly:
        os.remove(typeAndClickPath(directory))