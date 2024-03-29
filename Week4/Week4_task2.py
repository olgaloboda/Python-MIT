# part of the word game

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    copyHand = hand.copy()
    word = sorted(word)
    for w in word:
        if w in copyHand.keys():
            if copyHand[w] != 0:
                copyHand[w] -= 1
    
    return copyHand