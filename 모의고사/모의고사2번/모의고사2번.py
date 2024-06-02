# 정수 n을 입력받아 n각형의 대각선의 개수를 출력하도록 한 줄을 수정해 코드를 완성해 주세요.

n = int(input())

num_diagonal = n * (n - 3) / 2

print(int(num_diagonal))
