def solution(times, n):
    # 1. 공부한 시간 합의 최댓값을 저장할 정수 max_time을 만들고 0을 저장합니다.
    # 2. i를 0부터 times의 길이 - n 까지 1씩 증가시키며 아래 과정을 반복합니다.
    #   2-1. times[i]부터 n일동안 공부한 시간 합을 저장할 정수 val_sum을 만들고 0을 저장합니다.
    #   2-2. j를 i부터 i + n - 1 까지 1씩 증가시키며 아래 과정을 반복합니다.
    #     2-2-1. val_sum에 times[j]를 더합니다.
    #   2-3. 만약 max_time보다 val_sum이 더 크다면 max_time에 val_sum의 값을 저장합니다.
    # 3. max_time을 return합니다.
    max_time = 0
    for i in range(len(times) - n + 1):
        val_sum = 0
        print(i)
        for j in range(i, i + n):
            val_sum += times[j]
        if max_time < val_sum:
            max_time = val_sum
    return max_time


print(solution([4, 6, 3, 1, 0, 5, 9, 0, 1, 3], 4))
