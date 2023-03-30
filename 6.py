def IsSymmetric(n):
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] != matrix[j][i]:
               return False
    return True

print(IsSymmetric(3))