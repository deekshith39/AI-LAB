import copy,math

goal = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]
# src = [[1, 4, 2],
#        [3, 7, 5],
#        [6, 0, 8]]

#USING HEURISTIC FUNCTION (Manhattan Distance)


def index(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def manhattan(temp):
    sum = 0
    for i in range(3):
        for j in range(3):
            if temp[i][j] != 0:
                b = index(temp,temp[i][j])
                c = index(goal,temp[i][j])
                sum += abs(b[0] - c[0]) + abs(b[1] - c[1])
    return sum

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



def solve(visited,limit,src):
    if src == goal :
        print("Required moves to reach the goal state : " + str(limit))
        return True
    if limit > 120 :
        return False
    min = math.inf
    visited.append(src)
    possible_actions = possible_moves(src,visited)
    new_move = []
    for action in possible_actions:
        man_dist = manhattan(action)
        if action not in visited and man_dist < min :
            min = man_dist
            new_move = action
    print("Move : ",limit + 1)
    print_matrix(new_move)
    print()
    if solve(visited,limit+1,new_move) is True:
        return True
    else:
        return False

def print_matrix(mat):
    for i in mat:
        print(i)

if __name__ == '__main__':
    limit = 0
    visited = []
    src = []
    print("Enter the source state : ")
    for i in range(3):
        a = list(map(int,input().split()))
        src.append(a)
    print()
    print("***Heuristic Function***")
    print()
    print("Goal State : ")
    print_matrix(goal)
    print()
    print("Source State : ")
    print_matrix(src)
    print()
    if solve(visited,limit,src) is True:
        print("The puzzle has been solved!")
    else:
        print("It is impossible to solve the puzzle!")




