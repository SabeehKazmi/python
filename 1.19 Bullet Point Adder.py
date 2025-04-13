# The "1.19 Bullet Point Adder.py" script will get the text from the clipboard, 
# add a star and space to the beginning of each line, and then paste this new text to the clipboard. 
'''
In general, what this script will do;
    Paste text from the clipboard.
    Do something to it.
    Copy the new text to the clipboard.
'''
import sys, pyperclip
text=pyperclip.paste()
lines=text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text='\n'.join(lines)
pyperclip.copy(text)