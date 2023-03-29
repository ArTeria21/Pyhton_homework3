def IsSymmetric(n):
    matrix = []
    counter = 0
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == matrix[j][i]:
               counter += 1
    return counter

print(IsSymmetric(3))