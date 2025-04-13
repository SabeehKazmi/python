# copying and pasting strings with pyperclip() module
# 1. in terminal, first install pyperclip
# > pip install pyperclip

# 2. import pyperclip in your python program
import pyperclip

# copy to clipboard
# pyperclip.copy("Hello, Friend!")

# copy from clipboard
text = pyperclip.paste()
# print(text) # to run this we need to comment the .copy() method

# multi clipboard (saving different repeated sentences for quick use)
# read the following description about this program from the "Automating boring stuff with Python" book
'''
You want to be able to run this program with a command line argument that is a short key phrase—for instance, agree or busy. 
The message associated with that key phrase will be copied to the clipboard so that the user can paste it into an email. 
This way, the user can have long, detailed messages without having to retype them.
'''
# let's create a dictionary first
dick = {
    'busy':'Hi!\n I\'m extremely busy right now. I\' reach out ASAP just give me some time.\n Thank you!',
    'available':'Greetings!\n I am available and will be in touch ASAP. \n Thank you!',
    'fuckoff':'Hi!\n I\'ve no interest talking to you. Please go away! No thanks... Thug life forever!\n Regards, \n - Name'
}

# handling command line arguments
# we will use sys.argv to pass commands to our python program
import sys
# sys.argv[0] is always your python program name

# check if the user provided an argument
if len(sys.argv) < 2:
    print("Usage: 1.18 Copy and Paste Strings.py [key]")
    sys.exit()

key=sys.argv[1] # the key entered in the command line

# copy the message if the key exists
if key in dick:
    pyperclip.copy(dick[key])
    print(f"Message for '{key}' copied to clipboard!")
else:
    print(f"No message found for key: '{key}'")

# run the program in powershell like | python "1.18 Copy and Paste Strings.py" available
