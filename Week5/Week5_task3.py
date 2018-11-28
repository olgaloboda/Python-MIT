# part of the shift dictionary

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        for s in range(0, 25):
            bestShift = 26 - s
            message = self.apply_shift(bestShift).split()
            for m in message:
                if is_word(self.valid_words, m):
                    return (bestShift, self.apply_shift(bestShift))
        '''
        decypher = []
        max_word = 0
        for s in range(0, 25):
            shift = 26 - s
            count = 0
            message = self.apply_shift(shift).split()
            for m in message:
                if is_word(self.valid_words, m):
                    count += 1
            if max_word < count:
                max_word = count
                decypher = message
                bestShift = shift
                if bestShift == 26:
                    bestShift = 0
        return (bestShift, ' '.join(decypher))