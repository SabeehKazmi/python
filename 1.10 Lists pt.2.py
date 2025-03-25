cats = []
while True:
    print('Enter your cat\'s name or press \'q\' to quit either enter an existing name to remove it: ')
    user_input = input()
    if user_input == 'q':
        for i in range(len(cats)):
            print(cats[i], end=' ---> ')
        break
    else:
        for i in range(len(cats)):
            if user_input == cats[i]:
                print('Cat already exsits... meaow!')
                cats.remove(user_input)
                break
        cats.append(user_input)