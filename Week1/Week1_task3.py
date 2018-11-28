# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.

string = ''
previous_string = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
new = 0
prev = 0

# go through the word
for char in s:
    
    # reset the letter index to 0
    new = 0
    
    # take the first letter from the word and start looping through the alphabet
    for a in alphabet:
        
        # remember the index of a letter
        new += 1
        
        if char == a:
            
            # if the alphabet index is greater than the preceding one
            if prev > new:
                if len(string) > len(previous_string):
                    previous_string = string
                string = '' 
            
            string += char
            
            prev = new
            break
        
if previous_string == '' or len(previous_string) < len(string):
    previous_string = string
    
print("Longest substring in alphabetical order is: {}".format(previous_string))