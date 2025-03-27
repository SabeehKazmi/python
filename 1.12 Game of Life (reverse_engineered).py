# Conway's Game of Life
import random, time, copy

# # why copy? because we will be using copy.deepcopy()
# # what is copy.deepcopy()? To understand this we have the following program "terminate"
# # program "terminate" starts
# you = {'name': 'Hassan', 'skills': ['c++', 'C#', 'Python']} #nested data structure with a string and list
# _copy = copy.copy(you)
# _deepcopy = copy.deepcopy(you)
# you['skills'].append('JS')
# print(_copy) # output {'name': 'Hassan', 'skills': ['c++', 'C#', 'Python', 'JS']}
# print(_deepcopy) # output {'name': 'Hassan', 'skills': ['c++', 'C#', 'Python']}
# # the deepcopy will remain untouched and in its original state. it's used e.g., to save game states
# # program "terminate" ends

# represent grid
HEIGHT = 20
WIDTH = 60

# # to understand the grid better let's run a little program
# # starts
# for a in range(HEIGHT):
#     for b in range(WIDTH):
#         print('*', end='')
#     print() #this print will perform as enter (next line)
# # ends

# Initialize grid
nextcell = []
for x in range(WIDTH):
    col = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            col.append('#')  # Alive
        else:
            col.append(' ')  # Dead
    nextcell.append(col)

while True:
    print('\n' * 5)
    currentcell = copy.deepcopy(nextcell)

    # Print current state
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentcell[x][y], end='')
        print()

    # Update cells based on rules
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Count alive neighbors
            alive_neighbors = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
                        if currentcell[nx][ny] == '#':
                            alive_neighbors += 1

            # Apply Conway's rules
            if currentcell[x][y] == '#' and (alive_neighbors == 2 or alive_neighbors == 3):
                nextcell[x][y] = '#'
            elif currentcell[x][y] == ' ' and alive_neighbors == 3:
                nextcell[x][y] = '#'
            else:
                nextcell[x][y] = ' '

    time.sleep(1)
