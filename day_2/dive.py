with open('directions.txt') as f:
    lines = f.readlines()

depth = 0
horizontal = 0
for line in lines:
    line = line.strip()
    direction = line.split(" ")[0]
    value = int(line.split(" ")[1])
    if direction == "up":
        depth -= value
    elif direction == "down":
        depth += value
    else:
        horizontal += value

ans_1 = depth * horizontal
print(ans_1)

depth = 0
horizontal = 0
aim = 0
for line in lines:
    line = line.strip()
    direction = line.split(" ")[0]
    value = int(line.split(" ")[1])
    if direction == "up":
        aim -= value
    elif direction == "down":
        aim += value
    else:
        horizontal += value
        depth += aim*value

ans_2 = depth * horizontal
print(ans_2)

