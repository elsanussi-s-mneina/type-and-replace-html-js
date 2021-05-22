
# Uses template.html as a template, and replaces some text in it to make a new web page.
# for a language.

def fillTemplate(dirName: str, templateFileContents: str, scriptContents: str):
    """
    This function takes the contents of a template,
    and replaces some text in the template,
    and returns the result (the contents of the generated file).

    It does not write or edit any files.    
    """
    # Read the name of the orthography, e.g. German,
    # from a file.
    orthographyName: str = open(dirName + '/name.txt').read()
    
    # Replace the places in the template where an orthography
    # name occur with the one we want.
    titled: str = templateFileContents.replace('ISO-233 Arabic Romanization Template', orthographyName)

    
    # Read the list of replacements (necessary for functionality of the web application)
    # (really this is just a list of lists in Javascript (of string elements))
    replacements: str = open(dirName + '/replacements.txt').read()

    # Replace the place in the template where the replacements 
    # occur with the replacement list we want.
    scriptContentsWithReplacements =  scriptContents.replace('[[\'11\', \'2\']]', replacements)

    # Replace the place in the template where the script should go.
    withScript = titled.replace('/* PUT Script HERE */', scriptContentsWithReplacements)

    return withScript