# cats = []
# while True:
#     print('Enter your cat\'s name or press \'q\' to quit either enter an existing name to remove it: ')
#     user_input = input()
#     if user_input == 'q':
#         for i in range(len(cats)):
#             print(cats[i], end=' ---> ')
#         break
#     else:
#         for i in range(len(cats)):
#             if user_input == cats[i]:
#                 print('Cat already exsits... meaow!')
#                 cats.remove(user_input)
#                 continue # stops the loop or if right there and restarts it
#         cats.append(user_input)

# instead of using range(len(ls)) we use enumerate which gives index + value. 
ls = [4, 2, 3, 4, 5]
for i, x in enumerate(ls):
    print(ls[i])

#random.choice() and random.shuffle() on lists
import random
print(str(random.choice(ls)))
print('-->')
random.shuffle(ls)
print(ls)

# ls += 1 operator works similarly as ls = ls + 1

# index() method to search index of something within list
ls.index(2) # output: 1

