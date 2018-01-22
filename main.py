board = [
        [0, 40, 40, 40, 40, 0],
        [20, 0, 0, 0, 0, 40],
        [20, 0, 0, 0, 0, 40],
        [0, 20, 20, 20, 20, 0]
        ]

# The values that can change:
variables = [(1,1), (1,2), (1,3), (1,4), (2,1), (2,2), (2,3),
        (2,4)]

# Get surrounding points' temperature
def getSurroundings(point):
    row = point[0]
    column = point[1]

    if (column == 0):
        left = 0
    else:
        left = board[row][column-1]

    if (row == 0):
        top = 0
    else:
        top = board[row-1][column]

    if (column == len(board[row]) - 1):
        right = 0
    else:
        right = board[row][column+1]

    if (row == len(board) - 1):
        bottom = 0
    else:
        bottom = board[row+1][column]

    return (left, top, right, bottom)

def update():
    for v in variables:
        sr = getSurroundings(v)
        board[v[0]][v[1]] = (sr[0] + sr[1] + sr[2] + sr[3]) / 4

# Experiment starts here!
for i in range(100):
    update()

    for v in variables:
        print("{0: 7.4f}".format(board[v[0]][v[1]]), end=" ")
    print()
