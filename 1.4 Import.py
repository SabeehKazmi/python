import random, sys
# # ending the program with sys.exit()
# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')

# guess the number program
rand_int = random.randint(1, 20)
counter = 0
while True:
    print('Im thinking of a number b/w 1 and 10. Take a guess:')
    guess = input()
    if int(guess) < rand_int:
        print('You guessed lower.')
        counter = counter + 1
    elif int(guess) > rand_int:
        print('You guessed higher.')
        counter = counter + 1
    else:
        print('Great job, ' + str(rand_int) + ' is the number.')
        counter = counter + 1
        print('You took ' + str(counter) + ' guesses.')
        sys.exit()
