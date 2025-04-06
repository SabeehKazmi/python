# need an introduction? I don't think so, let's go straight to the code, brother
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