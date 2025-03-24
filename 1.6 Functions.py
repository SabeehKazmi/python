# simple function
def hello(name):
    print('Hello, ' + name + '!')
hello('Hassan')

# function with return value
import random
def fortune(num):
    if num == 1:
        return 'Do it!'
    elif num == 2:
        return 'Think about it!'
    elif num ==3:
        return 'Don\'t do it!'
random_number = random.randint(1,3)
print(fortune(random_number))

# print function with format
print('Arsenal', 'Manchester', 'Chelsea', sep=', ', end=' ') #sep is separator, end is end of line
print('are English football clubs.')

#FILO (First In Last Out) stack
def stack():
    stack = []
    stack.append('A')
    stack.append('B')
    stack.append('C')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
stack()

#FIFO (First In First Out) queue | this version is not clow but simplified for your learning. See 1.8 to learn more
def queue():
    queue = []
    queue.append('A')
    queue.append('B')
    queue.append('C')
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))
queue()

# local and global variables
global_var = 20
def local():
    x = 10
    print(global_var)
    print(x)
local()

# error handling
try:
    print(10/0)
except ZeroDivisionError:
    print('Error: Division by zero!')

# global statement
def sample_func():
    global some
    some = 'changed with global statement'
some = 'value'
sample_func()
print(some)

