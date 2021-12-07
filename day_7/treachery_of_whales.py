with open('positions.txt') as f:
    lines = f.readlines()

positions = list(map(lambda x: int(x), lines[0].split(",")))
positions.sort()
median = positions[len(positions)//2]
mean = sum(positions)//len(positions)
fuel_used = 0
for pos in positions:
    fuel_used += abs(pos - median)

ans_1 = fuel_used
print(ans_1)

fuel_used = 0
for pos in positions:
    end_num = abs(pos - mean)
    fuel_used += ((end_num + 1) * (end_num) // 2)

ans_2 = fuel_used
print(ans_2)