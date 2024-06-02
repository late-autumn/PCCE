def solution(key, original):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    answer = ""

    for i in range(len(original)):
        if original[i] == " ":
            answer += " "
            continue
        num_original = alphabet.index(original[i])
        num_key = alphabet.index(key[i % len(key)])

        # print(num_key)
        num_cryptogram = (num_original + num_key) % 26
        answer += alphabet[num_cryptogram]
    return answer

print(solution("bus", "today is sunday"))
