def solution(data, ext, val_ext, sort_by):
    answer = []
    dataInfo = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    for i in data:
        if i[dataInfo[ext]] < val_ext:
            answer.append(i)

    answer.sort(key=lambda x: x[dataInfo[sort_by]])
    return answer

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))
