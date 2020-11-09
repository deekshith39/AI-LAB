import copy

c = [0]

def printSolutionRoute(route):
    print("Solution: ")
    for step, state in enumerate(route):
        print("Step: ", step+1)
        print_matrix(state)

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


def dfs(curr, goal, visited, moves):
    if curr == goal :
        printSolutionRoute(visited)
        #print("Number of moves taken to solve 8 puzzle is : " + str(moves))
        return True
    if moves >= 12 :
        return False
    visited = visited + [curr]

    actions = possible_moves(curr,visited)

    for action in actions:
        if action not in visited:
            c[0] = c[0] + 1
            #print_matrix(action)
            if dfs(action, goal, visited, moves+1) is True:
                return True
    return False

if __name__ == '__main__':
    goal_state = [[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]]
    print("Using DFS Method ")
    print("Enter the source state : ")
    src = []
    for i in range(3):
        temp = list(map(int, input().split()))
        src.append(temp)
    print("Goal State : ")
    print_matrix(goal_state)
    print()
    print("Source State: ")
    print_matrix(src)
    visited = []

    if dfs(src,goal_state,visited,0) is True:
        print("Goal State : ")
        print_matrix(goal_state)
        print("Puzzle has been solved in " + str(c[0]+1) + " moves")
    else:
        print("It is impossible to solve the puzzle!")
