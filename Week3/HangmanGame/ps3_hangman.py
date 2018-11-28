# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
#for letters in string.ascii_lowercase:
#        if not lettersGuessed:
#            break
#        elif letters == lettersGuessed[0]:
#            string.ascii_lowercase = string.ascii_lowercase.replace(letters,'')
#            lettersGuessed = lettersGuessed[1:]
#    return string.ascii_lowercase

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    sum = 0
    for s in secretWord:
        for l in lettersGuessed:
            if l == s:
                sum += 1
                break
    print(sum)
    return sum == len(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter
        else:
            word += '_'
    return word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    line = ''
    for letters in string.ascii_lowercase:
        if letters not in lettersGuessed:
            line += letters
    return line

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round. max = 8

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    
    * The game should end when the user constructs the full word or runs out of 
      guesses. If the player runs out of guesses (s/he "loses"), reveal the 
      word to the user when the game ends.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = ''
    numGuess = 8
    print('Welcome to the game, Hangman!\nI am thinking of a word that is {} letters long'.format(len(secretWord)))
    while True:
        print('_____________')
        if numGuess > 1:
            print('You have {} guesses left'.format(numGuess))
        elif numGuess == 0:
            print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))
            break
        else:
            print('You have {} guess left'.format(numGuess))
        
        print('Available letters: {}'.format(getAvailableLetters(lettersGuessed)))
        
        letter = raw_input('Please guess a letter: ')
        
        if letter in lettersGuessed:
            print('Oops! You\'ve already guessed that letter: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
        elif letter in secretWord:
            lettersGuessed += letter
            print('Good guess: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
        else:
            lettersGuessed += letter
            numGuess -= 1
            print('Oops! That letter is not in my word: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
        
        if isWordGuessed(secretWord, lettersGuessed):
            print('_____________')
            print('Congratulations, you won!')
            break
    
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
