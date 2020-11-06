import copy,math

#USING ITERATIVE DEEPENING SEARCH

visited = []


def printBoard(board):
    for row in board:
        print(row)


def printSol(route):
    print("Solution: ")
    for step, state in enumerate(route):
        print("Step: ", step)
        printBoard(state)

def index(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def gen(temp,dir,b):
    t = copy.deepcopy(temp)
    if dir == 'u':
        t[b[0]][b[1]], t[b[0] - 1][b[1]] = t[b[0] - 1][b[1]], t[b[0]][b[1]]
    elif dir == 'd':
        t[b[0]][b[1]], t[b[0] + 1][b[1]] = t[b[0] + 1][b[1]], t[b[0]][b[1]]
    elif dir == 'l':
        t[b[0]][b[1]], t[b[0]][b[1] - 1] = t[b[0]][b[1] - 1], t[b[0]][b[1]]
    elif dir == 'r':
        t[b[0]][b[1]], t[b[0]][b[1] + 1] = t[b[0]][b[1] + 1], t[b[0]][b[1]]
    return t

def possible_moves(temp,visited):
    possible_mvs = []
    b = index(temp,0)
    direction = []
    if b[0] < 2 :
        direction.append('d')
    if b[0] > 0 :
        direction.append('u')
    if b[1] < 2 :
        direction.append('r')
    if b[1] > 0 :
        direction.append('l')

    for i in direction:
        move = gen(temp,i,b)
        if move not in visited:
            possible_mvs.append(move)

    return possible_mvs


def dfs(curr, goal, visited, depth):
    if curr == goal:
        return True
    if depth <= 0:
        return False
    visited = visited + [curr]

    actions = possible_moves(curr,visited)

    # print("Move " + str(moves))
    # print_matrix(curr)

    for action in actions:
        if action not in visited:
            print()
            print_matrix(action)
            print()
            flag = dfs(action, goal, visited , depth-1)
            if flag == True:
                return True

def iddfs(curr, goal):
    #visited = []
    depth = 1
    while True:
        print("Depth : " + str(depth))
        print()
        print_matrix(curr)
        print()
        if dfs(curr, goal, visited, depth) is True:
            return depth
        else:
            depth += 1

def print_matrix(mat):
    for i in mat:
        print(i)
    print()

if __name__ == '__main__':
    goal = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]]
    # src = [[1, 4, 2],
    #        [3, 7, 5],
    #        [6, 0, 8]]
    print("GOAL STATE")
    print_matrix(goal)
    src = []
    print("Iterative Deepening")
    print("Enter the source state : ")
    for i in range(3):
        a = list(map(int, input().split()))
        src.append(a)

    print("INITIAL STATE : ")
    print_matrix(src)

    depth = iddfs(src,goal)
    if depth:
        print("The Puzzle is solved at depth " + str(depth))










