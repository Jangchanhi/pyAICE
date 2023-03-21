# 그리디 알고리즘
# 3-1 거스름돈 문제

money = 0
count = 0
coins = [500, 100, 50, 10]


print("점원에게 줄 돈은 얼마인가요?")
money = int(input("돈 : "))
print(money)

for coin in coins:
    count += money // coin
    money %= coin

print("동전의 개수")
print(count)










