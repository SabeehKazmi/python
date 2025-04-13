# copying and pasting strings with pyperclip() module
# 1. in terminal, first install pyperclip
# > pip install pyperclip

# 2. import pyperclip in your python program
import pyperclip

# copy to clipboard
pyperclip.copy("Hello, Friend!")

# copy from clipboard
text = pyperclip.paste()
print(text)

