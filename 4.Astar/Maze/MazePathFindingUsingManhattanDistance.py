import math

path = []
closedPath = []
neighbours = [[-1, -1],[-1, 0],[-1, 1],[0, -1],[0, 1],[1, -1],[1, 0],[1, 1]]

def Manhattan(action, src, dest):
    #currstate - goalstate coordinates
    return abs(action[0] - (dest[0]-1)) + abs(action[1] - (dest[1]-1))

def ShortestDistance(actions, src, dest):
    min = math.inf

    for action in actions:
        if Manhattan(action,src,dest) < min:
            move = action
            min = Manhattan(action,src,dest)
    return move

def possible_moves(mat, curr, n, m):
    possible_mvs = []
    for x in neighbours:
        a = []
        a.append(curr[0] + x[0])
        a.append(curr[1] + x[1])
        if a[0] > -1 and a[0] < n and a[1] > -1 and a[1] < m :
            if mat[a[0]][a[1]] :
                if a not in path and a not in closedPath:
                    possible_mvs.append(a)

    return possible_mvs

def findPath(mat, n, m, src, dest):
    curr = [src[0]-1, src[1]-1] #starting position
    path.append(curr)

    while curr != [dest[0]-1, dest[1]-1]:
        actions = possible_moves(mat, curr, n, m)

        if actions:
            curr = ShortestDistance(actions,src,dest)
            path.append(curr)
        else: #if no moves are possible from present location
            if path:
                closedPath.append(curr)
                path.pop()
                if path:
                    curr = path[len(path) - 1]
                else:
                    print("No Path!")
                    exit(0)
            else:
                print("No Path!")
                exit(0)

def main():
    print("Enter the number of rows : ")
    n = int(input())
    print("Enter the number of columns : ")
    m = int(input())

    print("Enter the Matrix : (0 - blocked,1 - free)")
    mat = []
    for i in range(n):
        temp = list(map(int,input().split()))
        mat.append(temp)
    print()
    print("Enter the source and the destination coordinates : ")
    src = list(map(int,input().split()))
    dest = list(map(int,input().split()))

    findPath(mat, n, m, src, dest)
    print()
    print("The PATH :")
    print("'-' represents the path")
    print()
    for i in range(n):
        for j in range(m):
            if [i,j] in path :
                print("-",end=" ")
            else:
                print(mat[i][j],end=" ")
        print()


if __name__ == '__main__':
    main()