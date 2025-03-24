# simple print statement
print ('Hello, World!')

# simple print statement with a variable
name = 'Hassan'
print ('This is ' + name + ' to the rescue!')
# if-else with user input
password = 'death'
print('Enter your password:')
user_password = input()
if user_password == password:
    print('Access Granted')
else:
    print('Access Denied')

# example; data types and type conversion
(12 + 2.5) / 1.33
2 ** 3 #power
4 % 3 #reminder
'uou' * 5 #string multiplication
len(name) #string length

# this '# %%' is used to separate code blocks in Jupyter Notebook

# input format
your_age = input('Enter your age: ')
print ('You will be ' + str(int(your_age) + 1) + ' in a year.')