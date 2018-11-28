# part of a Hangman game task

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    
    myDict = {}
    sum = 0
    for s in secretWord:
        if s in myDict:
            myDict[s] += 1
        else:
            myDict[s] = 1
    for l in lettersGuessed:
        if l in myDict.keys():
            sum += 1
    return sum == len(secretWord)
    sum = 0
    '''
    sum = 0
    for s in secretWord:
        for l in lettersGuessed:
            if l == s:
                sum += 1
                break
    return sum == len(secretWord)