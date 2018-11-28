# part of the Hangman game

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
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
        
        letter = input('Please guess a letter: ')
        
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