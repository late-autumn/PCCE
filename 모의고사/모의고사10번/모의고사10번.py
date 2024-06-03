def solution(snippet, message):
    answer = ''
    words = message.split(" ")

    for w in words:
        msg = w
        for s in snippet:
            if s[0] == msg:
                msg = s[1]
                break
        answer += msg + " "
    return answer


print(solution([["IMO,", "In my opinion,"], ["AYS?", "Are you serious?"], ["TTYL.", "Talk to you later."]],
               "IMO, it does not look so good. AYS? TTYL."))

print(solution([["IMO", "In my opinion"]], "IMO, IMO"))
