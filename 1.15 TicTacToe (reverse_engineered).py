# need an introduction? I don't think so, let's go straight to the code, brother
import sys
board = {
    'TL':'', 'TC':'', 'TR':'',
    'CL':'', 'CC':'', 'CR':'',
    'BL':'', 'BC':'', 'BR':''
}

def p_board(x):
    print('  ' + x['TL'] + ' | ' + x['TC'] + ' | ' + x['TR'])
    print('-----------')
    print('  ' + x['CL'] + ' | ' + x['CC'] + ' | ' + x['CR'])
    print('-----------')
    print('  ' + x['BL'] + ' | ' + x['BC'] + ' | ' + x['BR'])

p_board(board)

# winning conditions
chk_win = [
    ['TL','CL','BL'],
    ['TC','CC','BC'],
    ['TR','CR','BR'],
    ['TL','TC','TR'],
    ['CL','CC','CR'],
    ['BL','BC','BR'],
    ['TL','CC','BR'],
    ['BL','CC','TR']
]

# quick win check
def win_check(current_brd_pos, player):
    for combo in chk_win:
        if all(current_brd_pos[pos] == player for pos in combo):
            return True
    return False

# main()
def ttt():
    current_player = 'X'
    cur_move_no = 0
    max_moves = 9

    while cur_move_no <= max_moves:
        print('\n You\'re (' + current_player + ') What\'s your move? Or press q to quit')
        plyr_mv = input()

        if plyr_mv == 'q':
            sys.exit()

        if plyr_mv not in board:
            print('Invalid!')
            continue

        if board[plyr_mv] != '':
            print('already taken!')
            continue
        
        board[plyr_mv] == current_player
        cur_move_no += 1
        p_board(board)

        if win_check(board, current_player):
            print('You win!' + current_player)
            break

        current_player = 'O' if current_player == 'X' else 'X'

    else:
        print('It\'s a tie')

# start game
ttt()