# part of the word game

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    value = False
    copyHand = hand.copy()
    for l in wordList:
        # if the word is in the wordList
        if word == l:
            value = True
            # loop through the letters in the word
            for w in word:
                # if the letter matches the key in a dictionary
                if w in copyHand.keys() and copyHand[w] != 0:
                    # decrease the letter index
                    copyHand[w] -= 1
                else:
                    value = False
    return value