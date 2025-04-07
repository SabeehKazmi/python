# upper() lower() isupper() and islower() methods
# uppercase, lowercase, is all uppercase, and is all lowercase respectively
name1 = "john"
name2 = "SMITH"
name3 = "AfzaL"
name4 = "Afzal"
print(name1.upper())
print(name2.lower())
print(name3.upper().lower())
if name1.islower():
    print("Behold! The power of this %s" % (name1))
"""
we use this for case sensitive matter when comparing two values, like AfzaL and Afzal are not the same but we can compare them easily.
there may be need to do so but if the need arise you exactly know how to handle this, for example checking the username
"""

# the isX() methods
# these methods returns a boolean value that describes the nature of the string
"""
isalpha() is only letters and not blank
isalnum() is only letters and numbers and not blank
isdecimal() is only numericals and not blank
isspace() is only spaces tabs and newlines and not blank
istitle() contains strings start is uppercase and followed by lower case and is not blank
"""
if name4.istitle():
    print("Afzal")
passwd = "Afzal1234"
if passwd.isalnum():
    print("Correct!")
num = "23"
if num.isdecimal():
    print("You got this!")
# you got the gist.

# startswith() and endswith() methods | these methods are self-explanatory
if name4.startswith('Af'):
    print("Yes!")
if passwd.endswith('34'):
    print("Same password again!!!")

# join() and split() methods
# you have seen the execution of join method before in "1.16 Strings" when we were getting elements from a string to create a new string
print(' - '.join([name1, name2, name3, name4]))
print('\n' * 2)
# split() does the opposite
print('John Smith'.split()) # e.g., firstname lastname
print('John_Smith'.split('_')) # same output you can even .split('\n') for a '''string_value''' string
print('\n')

# partition() method
# split string into three based on the passed parameter in partition('passed_parameter') e.g.,
str1 = 'PULL'
str2 = 'LASSY'
str3 = str1.partition('L')[0]
str4 = str2.partition('A')[2]
print(''.join([str3, str4])) # got any lately?

