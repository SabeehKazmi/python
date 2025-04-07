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

# startswith() and endswith() methods
