# part of the word game

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    i = 0
    for k in hand:
        i += hand[k]
    return i
    """
    return sum(hand.values())