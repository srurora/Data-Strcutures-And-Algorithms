#Search in a row and column wise sorted matrix
def searchInMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    i = 0
    j = cols - 1
    while i < rows and j >= 0:
        if matrix[i][j] == target: return True
        else:
            if matrix[i][j] > target: j-=1
            else: i-=1
    return False


if __name__ == "__main__":
    mat = [[10, 20, 30, 40], [15, 25, 35, 45],
           [27, 29, 37, 48], [32, 33, 39, 50]]

    # Function call
    if(searchInMatrix(mat, 10)):
        print("Found")
    else: print("Not Found")

    if(searchInMatrix(mat, 0)):
        print("Found")
    else: print("Not Found")