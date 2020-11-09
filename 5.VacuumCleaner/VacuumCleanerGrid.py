def clean(floor):
    row, col = len(floor), len(floor[0])
    for i in range(row):
        if i % 2 == 0:
            for j in range(col):
                if floor[i][j] == 1:
                    printMatrix(floor, i, j)
                    print("This cell is dirty")
                    floor[i][j] = 0
                    print("After cleaning, ")
                    printMatrix(floor, i, j)
                    print("Moving to next cell")
                    print()
                else:
                    printMatrix(floor, i, j)
                    print("This cell is clean,")
                    print("Moving to next cell")
                    print()
        else:
            for j in range(col - 1, -1, -1):
                if floor[i][j] == 1:
                    printMatrix(floor, i, j)
                    print("This cell is dirty")
                    floor[i][j] = 0
                    print("After cleaning, ")
                    printMatrix(floor, i, j)
                    print("Moving to next cell")
                    print()
                else:
                    printMatrix(floor, i, j)
                    print("This cell is clean, ")
                    print("Moving to next cell")
                    print()

def printMatrix(floor,row,col):
    n, m = len(floor), len(floor[0])
    for i in range(n):
        for j in range(m):
            if row == i and j == col:
                print("-" + str(floor[i][j]) + "-",end=" ")
            else:
                print(" " + str(floor[i][j]) + " ",end=" ")
        print()

def main():
    floor = []
    n = int(input("Enter the number of rows : "))
    m = int(input("Enter the number of columns : "))

    print("Print the floor Matrix [1 - dirty,0 - clean] : ")
    for i in range(n):
        temp = list(map(int,input().split()))
        floor.append(temp)

    print("The Vacuum Cleaner moves in a Zig-Zag fashion")
    print()
    clean(floor)

    print("All the places are clean!")
    printMatrix(floor,n-1,m-1)

if __name__ == '__main__':
    main()