# Type and Replace and Type and Click Web applications
 Makes replacements such as: a' (small letter a then apostrophe) becomes á (a with an acute accent): possible in a web browser without depending on installed keyboard layout.
 This is an input method for situations where installing the proper keyboard layout is inconvenient or impossible.

A simpler to use alternative without replacements is also provided: I call this type and click.

## Goals and Purposes:
The goal of this project is to facilitate input of text into the computer with the minimum of setup.

There are better ways to input all of these languages, but for people who are in situations where they use more than one computer, especially public ones it is often impossible to use these better ways. 

For those who do not know, for the more popular languages like Spanish there is almost always a keyboard layout provided by the software that comes with the computer. All one has to do is to go in to the settings, and enable it. This is possible even if the keyboard one types on labelled with the characters of another language.

Although ideal, using a system keyboard layout is often out of the question for many situations. In public places such as libraries, often only one keyboard layout is available. That is the user has no choice.

However, very few languages are written using exactly the same character set as another language. Even European languages using the same script use different characters such as C cedilla (ç), which are essential for correct spelling. For other languages which do not have a Latin orthography, the problem is even worse.

For this reason, people create web pages where a person can type these languages without having to change the keyboard layout in the Operating System. The most well known of these are virtual keyboards, which are web pages where the visual aspects and functionality of a real keyboard are duplicated within the confines of a web page.

Virtual keyboards are excellent for people who are already good typists in the language. For other people they have far more features than necessary. Also, virtual keyboards require far more programming effort.

A less full featured web application that does something similar is the textbox with a clickable buttons for characters that are not on an English keyboard. I call this the Type-and-Click web applications. These exist and are seen in many places.

I decided to try a slightly different idea. There are people who instead of relying on a keyboard layout simply have their operating system configured to replace certain character sequences. For example, Mac OS comes configured to replace "omw" with "on my way". So I made a web application that does this, but without the need to customize. Instead, I make one web application that has appropriate replacements for Polish, and another for Spanish. It also includes a legend displaying which replacements occur.

The main difficulty is designing the replacements in such a way that they are easy to remember, not likely ever to be needed as they are, and easy to type. In many situations, I chose the ampersand, for example for o and e squished together I chose "o&e" in many cases.


## User requirements
- a modern web browser with Javascript enabled

## Developer requirements
- Python 3.9 approximately
- Unix terminal
- a modern web browser running Javascript

## Various sub projects will be included
Currently implemented:
- ISO-233 Romanization (for Arabic)
- Spanish
- Portuguese
- Berber Latin Alphabet
- French
- Modern South Arabian Languages in Arabic script: Mehri and Soqotri
- German
- Latin (both macron and acute accent are supported)
- Maltese
- Pinyin
- Polish
- Buckwalter transliteration system for Arabic
  - For typing Arabic script using Latin characters
  - For converting Arabic script into Buckwalter latin
- Scottish Gaelic (including acute accent)

## How to run the generator in Unix like OS:

1. Open the terminal.
2. Change the permissions by running the following command:

`chmod +x generateWebPages.sh`

3. Run the shell script by running the following command.
`./generateWebPages.sh`

4. Go to the folder titled "generated" in the current directory. It should contain all the files you are looking for. They should be HTML files that you can run in a web browser.