f = open("input.txt", "r")
calories = 0
result = []
x = f.readline()
while x != "end":
    while x != "":
        calories = calories + int(x)
        x = f.readline().rstrip()
    result.append(calories)
    calories = 0
    x = f.readline().rstrip()
maxValue = max(result)
print(result)
print(maxValue)
result.remove(maxValue)
maxValue2 = max(result)
print(maxValue2)
result.remove(maxValue2)
maxValue3 = max(result)
print(maxValue3)
result2 = maxValue + maxValue2 + maxValue3
print(result2)