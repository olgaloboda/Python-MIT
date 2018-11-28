# part of the Hangman game task

import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    line = ''
    for letters in string.ascii_lowercase:
        if letters not in lettersGuessed:
            line += letters
    return line