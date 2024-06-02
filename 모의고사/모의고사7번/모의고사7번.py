# 상자 무게
def func1(weight):
    if weight < 5:
        return 500
    elif weight < 10:
        return 1000
    else:
        return 4000


# 상자 크기
def func2(w, l, h, we):
    if w >= 80 or l >= 80 or h >= 80:
        return -1
    if w + l + h >= 160:
        return -1
    if we >= 25:
        return -1
    return 0


def func3(size):
    if size < 80:
        return 3500
    elif size < 100:
        return 4500
    elif size < 120:
        return 6000
    else:
        return 12000


def solution(width, length, height, weight):
    if func2(width, length, height, weight):
        return -1
    price = func1(weight)
    price += func3(width+length+height)

    return price


print(solution(40, 30, 70, 14))
print(solution(30, 20, 90, 5))