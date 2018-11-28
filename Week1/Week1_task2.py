# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print Number of times bob occurs is: 2
i = 0
num = 0

for char in s:
    if char == 'b':
        if string == 'bo':
            string += 'b'
            num += 1
        string = 'b'
    elif char == 'o' and string == 'b':
        string += 'o'
    else:
        string = ''

    
print("Number of times bob occurs is: {}".format(num))