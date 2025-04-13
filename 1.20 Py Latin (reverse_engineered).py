# pig latin is a madup language that alters english words
print('Enter something to be convered into Py Latin:\n')
message=input()
VOWELS=['a','e','i','o','u','y'] # 'y' is sometimes a vowel (learn more from your fingers on a keyboard)
PyLatin=[] # this will store all the translated words.
for word in message.split(): # this will split the message into words
    # handle punctuation at start of the words
    prefixNonLetters='' 
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters+=word[0]
        word=word[1:] # chops off the first character
    if len(word) == 0:
        PyLatin.append(prefixNonLetters) # if the word is all symbols, then keep the symbols and continue
        continue
    # handle punctuation at end of the words
    suffixNonLetters=''
    while not word[-1].isalpha():
        suffixNonLetters=word[-1]+suffixNonLetters
        word=word[:-1] # Example: "hello!!!" → stores !!! and keeps hello for now
    # remember the case
    wasUpper=word.isupper()
    wasTitle=word.istitle()
    # convert the word to lower-case to work with easily
    word=word.lower()
    # extract starting consonances
    prefixConsonants=''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants+=word[0]
        word=word[1:]
    # PyLatin rules
    if prefixConsonants!='':
        word+=prefixConsonants+'fu'
    else:
        word+='fuuck'
    # restore original case
    if wasUpper:
        word=word.upper()
    if wasTitle:
        word=word.title()
    # add back any punctuations to the word
    PyLatin.append(prefixNonLetters+word+suffixNonLetters)
    # combines all the words into a sentence
print(' '.join(PyLatin))
