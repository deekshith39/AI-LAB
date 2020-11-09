import copy

def print_matrix(mat):
    for row in mat:
        print(row)
    print()

def index(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i,x.index(v))

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

def possible_moves(temp, visited):
    possible_mvs = []
    b = index(temp,0)
    direction = []

    if b[0] < 2:
        direction.append("d")
    if b[0] > 0:
        direction.append("u")
    if b[1] < 2:
        direction.append("r")
    if b[1] > 0:
        direction.append("l")

    for i in direction:
        move = gen(temp,i,b)
        if move not in visited:
            possible_mvs.append(move)

    return possible_mvs



def BFS(curr, goal, visited):
    moves = 1
    frontier = []
    visited.append(curr)
    frontier.append(curr)

    while True:
        temp = frontier.pop(0)
        # if(temp == goal):
        #     print_matrix(temp)
        #     print("The Puzzle is solved in " + str(moves) + " moves")
        #     print("Successful! ")
        #     return True
        if moves > 120:
            return False

        actions = possible_moves(temp,visited)

        for action in actions:
            if action not in visited:
                print("Step "+str(moves)+" :")
                print_matrix(action)
                if action == goal:
                    print("The puzzle has been solved after " + str(moves) + " moves")
                    print("Successful!")
                    return True
                moves += 1
                visited.append(action)
                frontier.append(action)


if __name__ == '__main__':
    print("**Using BFS**")
    goal_state = [[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]]
    print("GOAL STATE : ")
    print_matrix(goal_state)

    print("Enter the source state : ")
    src = []
    for i in range(3):
        temp = list(map(int, input().split()))
        src.append(temp)

    print("Source State : ")
    print_matrix(src)
    visited = []
    if BFS(src, goal_state, visited) is True:
        print("The Puzzle has been Solved!")
    else:
        print("It is Impossible to solve the puzzle")