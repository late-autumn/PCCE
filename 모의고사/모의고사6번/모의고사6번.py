def solution(matrix_A, matrix_B):
    answer = []
    for i in range(len(matrix_A)):
        row = []
        for j in range(len(matrix_A[i])):
            row.append(matrix_A[i][j] +matrix_B[i][j])
        answer.append(row)
    return answer


print(solution([[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[0, 1, 1], [1, 0, 0], [0, 0, 1]]))
