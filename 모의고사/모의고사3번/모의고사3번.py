# 문제
# 민철이는 국비 지원을 받아 프로젝트에 참가해 코딩 공부를 시작했습니다. 국비 지원은 나이 별로 다음과 같이 할인을 해줍니다.
# 20~29세: 90% 할인
# 30~39세: 70% 할인
# 그 외: 100% 할인
# 또, 만약 프로젝트를 모두 수료한다면 지불 금액의 50%를 돌려줍니다.
# 민철이의 나이 age, 프로젝트의 원래 금액 money, 수료 여부 complete가 정수 입력으로 주어질 때, 민철이가 최종적으로 지불한 금액을 출력하도록 빈칸을 채워 코드를 완성해주세요.

age = int(input())
money = int(input())
complete = int(input())

if age >= 20 and age < 30:
    money = money // 100 * 10
elif age >= 30 and age < 40:
    money = money // 100 * 30
else:
    money = 0

if complete == 1:
    money = money // 2

print(money)
