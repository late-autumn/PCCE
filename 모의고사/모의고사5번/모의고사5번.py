def solution(menu, n):
    tomato_pasta = [4, 4, 1, 125]
    shrimp_oil_pasta = [6, 3, 0, 170]
    mushroom_cream_pasta = [5, 4, 1, 140]
    answer = [0, 0, 0, 0]
    if menu == "tomato pasta":
        for i in range(4):
            answer[i] = tomato_pasta[i] * n

    elif menu == "shrimp oil pasta":
        for i in range(4):
            answer[i] = shrimp_oil_pasta[i] * n

    elif menu == "mushroom cream pasta":
        for i in range(4):
            answer[i] = mushroom_cream_pasta[i] * n
    return answer


print(solution("tomato pasta", 3))
print(solution("mushroom cream pasta", 12))
