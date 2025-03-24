# rock, paper, scissors game
import random, sys
print ('Rock Paper Scissors')
win = 0
lose = 0
draw = 0
while True:
    print ('Win: ' + str(win) + ' Lose:' + str(lose) + ' Draw:' + str(draw))
    print ('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
    player_input = input()
    ai_input = random.randint(1, 3) # 1 = rock, 2 = paper, 3 = scissors
    if player_input == 'q':
        sys.exit()
    elif player_input == 'r' or player_input == 'p' or player_input == 's':
        if player_input == 'r':
            print ('Rock versus...')
            if ai_input == 1:
                print ('Rock')
                print ('It is a draw!')
                draw += 1
            elif ai_input == 2:
                print ('Paper')
                print ('You lose!')
                lose += 1
            elif ai_input == 3:
                print ('Scissors')
                print ('You win!')
                win += 1
        elif player_input == 'p':
            print ('Paper versus...')
            if ai_input == 1:
                print ('Rock')
                print ('You win!')
                win += 1
            elif ai_input == 2:
                print ('Paper')
                print ('It is a draw!')
                draw += 1
            elif ai_input == 3:
                print ('Scissors')
                print ('You lose!')
                lose += 1
        elif player_input == 's':
            print ('Scissors versus...')
            if ai_input == 1:
                print ('Rock')
                print ('You lose!')
                lose += 1
            elif ai_input == 2:
                print ('Paper')
                print ('You win!')
                win += 1
            elif ai_input == 3:
                print ('Scissors')
                print ('It is a draw!')
                draw += 1
    else:
        print ('Invalid input.')