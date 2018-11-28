# part of the shift dictionary

import string
class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        myDict = {}
        i = shift
        for l in string.ascii_lowercase:
            if i < 26 :
                myDict[l] = string.ascii_lowercase[i]
            else:
                i = 0
                myDict[l] = string.ascii_lowercase[i]
            i += 1
        for u in string.ascii_uppercase:
            if i < 26 :
                myDict[u] = string.ascii_uppercase[i]
            else:
                i = 0
                myDict[u] = string.ascii_uppercase[i]
            i += 1
        return myDict

    def apply_shift(self, shift):
        caesarMessage = ''
        new_dict = self.build_shift_dict(shift)
        for s in self.message_text:
            if s in new_dict:
                caesarMessage += new_dict[s]
            else:
                caesarMessage += s
        return caesarMessage