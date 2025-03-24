# to un-comment ctrl + /
# while not loop
while not True:
    print('This will never print')
while not False:
    print('This will print')
    break
name = ''
while not name:
    name = input('Enter your name:')
print('Hello, {}'.format(name))

# for loop
print('Type a number:')
num = input()
for i in range(int(num)):
    print(i)

# for loop with a list
for i in [1, 2, 3, 4, 5]:
    print(i)

# for loop with a string
for i in 'hello':
    print(i)

# for loop with a dictionary
d = {'name': 'jane', 'age': 23}
for i in d:
    print(i)

# length
mylist = ["apple", "banana", "cherry"]
x = len(mylist) # 3

