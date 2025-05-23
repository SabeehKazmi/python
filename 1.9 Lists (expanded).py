# a simple list
todo = ['father', 'mother', 'sister']
todo.append('brother')
todo[1] = '-'
print(todo)
todo.remove('-')
print(todo)

# list with multiple indexes
mul_list = [['Hassan', 28, -1.8],['Sarmad', 29, -0.8]]
print(mul_list[0])
print(mul_list[1])
mul_list.append(['Zia', 34, -1.0])
print(mul_list[-1]) # select last elements from a list

# slicing the list
smp_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(smp_lst[1:4]) # e.g., [:] all [1:] from [:5] to
print(len(smp_lst)) # list length

# deleting with del and comparison with .remove
li_lst = ['H', 'S', 'Z']
# li_lst.remove(0) | it will not work as it can't remove values from index
# li_lst.remove('H') | it will work
del li_lst[0]
print(li_lst)

# a simple program with lists
import sys
cats = []
while True:
    print('Enter your cat name or press \'q\' to quit: ')
    cat = input()
    if cat == 'q':
        # print(cats[:]) | can be but i am using for loop for this one
        for c in range(len(cats)):
            print('Index #' + str(c) + ' is: ' + cats[c])
        break # or sys.exit() | I prefered this but the rest of the code will go void
    else:
        if cat not in cats: # check if the cat name is already in the list
            cats.append(cat)
        else:
            print('The name already exists.')

# in and not in operators for finding something in lists
a = 'meaow' in cats
b = 'meaow' not in cats
print(str(a))
print(str(b))
