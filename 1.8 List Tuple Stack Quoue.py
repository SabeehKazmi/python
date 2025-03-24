# list gives you fill control over the items
# remember, list and stack are the same until you use pop() and now python knows its a stack
todo_list = ['call home', 'do python', 'pray']
todo_list.remove('pray')
todo_list[0] = 'gym'
todo_list.append('another one')
print(todo_list) #output gym, do python, another one

# tuple for fixed data like user_id or creation date
user_info = ('Alice', 18) # user_info[0] = 'john' | Error: fixed
print(user_info)

# stack is LIFO behaviour
undo = []
undo.append('2nd last typed: Windows')
undo.append('Last typed: Userz')
print(undo.pop())
print(undo.pop())

#queue is FIFO behaviour
from collections import deque
queue = deque()
queue.append('user_1')
queue.append('user_2')
print(queue.popleft())
print(queue.popleft())

# why import deque? Because performance, fast. Here's why:
import time
#using list
queue_1 = list(range(20000))
start = time.time()
while queue_1:
    queue_1.pop(0)
    print(time.time() - start)
# using deque
queue_2 = deque(range(20000))
start = time.time()
while queue_2:
    queue_2.popleft()
    print(time.time() - start)
# you will see queue is about ~1.2 seconds faster in this case