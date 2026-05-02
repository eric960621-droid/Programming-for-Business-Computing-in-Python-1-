a = int(input())

change = 1000 - a

denominations = [500, 100, 50, 10, 5, 1]
result = []
for d in denominations:
    count = change // d 
    result.append(count)
    change %= d

print(*result) 
