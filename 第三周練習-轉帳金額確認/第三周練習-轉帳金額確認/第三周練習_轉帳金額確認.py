a = int(input())
change = 1000 - a

coins = [500, 100, 50, 10, 5, 1]

result = []

for coin in coins:
    count = change // coin   # 可以用幾張
    if count > 0:
        result.append(f"{coin}, {count}") #f-string:將變數塞進字串裡面(f"{coin}:{count}")
        change = change % coin   # 剩下的錢

print("; ".join(result))