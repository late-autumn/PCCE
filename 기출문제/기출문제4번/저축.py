start = int(input())
before = int(input())
after = int(input())

money = start
month = 1
while money < 70:
    money += before

    month += 1
while money < 100:
    month += 1
    money += after

print(month)
