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



# # Create a list of list for the cells:
# nextCells = []
# for x in range(WIDTH):
#     column = [] # Create a new column.
#     for y in range(HEIGHT):
#         if random.randint(0, 1) == 0:
#             column.append('#') # Add a living cell.
#         else:
#             column.append(' ') # Add a dead cell.
#     nextCells.append(column) # nextCells is a list of column lists.

# while True: # Main program loop.
#     print('\n\n\n\n\n') # Separate each step with newlines.
#     currentCells = copy.deepcopy(nextCells)

#     # Print currentCells on the screen:
#     for y in range(HEIGHT):
#         for x in range(WIDTH):
#             print(currentCells[x][y], end='') # Print the # or space.
#         print() # Print a newline at the end of the row.

#     # Calculate the next step's cells based on current step's cells:
#     for x in range(WIDTH):
#         for y in range(HEIGHT):
#             # Get neighboring coordinates:
#             # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
#             leftCoord  = (x - 1) % WIDTH
#             rightCoord = (x + 1) % WIDTH
#             aboveCoord = (y - 1) % HEIGHT
#             belowCoord = (y + 1) % HEIGHT

#             # Count number of living neighbors:
#             numNeighbors = 0
#             if currentCells[leftCoord][aboveCoord] == '#':
#                 numNeighbors += 1 # Top-left neighbor is alive.
#             if currentCells[x][aboveCoord] == '#':
#                 numNeighbors += 1 # Top neighbor is alive.
#             if currentCells[rightCoord][aboveCoord] == '#':
#                 numNeighbors += 1 # Top-right neighbor is alive.
#             if currentCells[leftCoord][y] == '#':
#                 numNeighbors += 1 # Left neighbor is alive.
#             if currentCells[rightCoord][y] == '#':
#                 numNeighbors += 1 # Right neighbor is alive.
#             if currentCells[leftCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-left neighbor is alive.
#             if currentCells[x][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom neighbor is alive.
#             if currentCells[rightCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-right neighbor is alive.

#             # Set cell based on Conway's Game of Life rules:
#             if currentCells[x][y] == '#' and (numNeighbors == 2 or
# numNeighbors == 3):
#                 # Living cells with 2 or 3 neighbors stay alive:
#                 nextCells[x][y] = '#'
#             elif currentCells[x][y] == ' ' and numNeighbors == 3:
#                 # Dead cells with 3 neighbors become alive:
#                 nextCells[x][y] = '#'
#             else:
#                 # Everything else dies or stays dead:
#                 nextCells[x][y] = ' '
#     time.sleep(1) # Add a 1-second pause to reduce flickering.