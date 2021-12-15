import re 

with open("instructions.txt") as f:
    lines = f.readlines()

coords = []
instructions = []
for line in lines:
    coord = re.match(r'([0-9]+)\,([0-9]+)', line.strip())
    instruction = re.match(r'fold along (.)=([0-9]+)', line.strip())
    if coord:
        x, y = coord.groups()
        coords.append((int(x), int(y)))
    elif instruction:
        instructions.append(instruction.groups())

coords1 = coords.copy()
for instruction in instructions[:1]:
    x_or_y, value = instruction
    value = int(value)
    if x_or_y == 'x':
        coords1 = [((2*value - x), y) if x >= value else (x, y) for x, y in coords1]
        coords1 = list(set(coords1))
    elif x_or_y == 'y':
        continue

ans_1 = len(coords1)
print(ans_1)

for instruction in instructions:
    x_or_y, value = instruction
    value = int(value)
    if x_or_y == 'x':
        coords = [((2*value - x), y) if x >= value else (x, y) for x, y in coords]
        coords = list(set(coords))
    elif x_or_y == 'y':
        coords = [(x, (2*value - y)) if y >= value else (x, y) for x, y in coords]
        coords = list(set(coords))

max_x = max([x for x, y in coords])
max_y = max([y for x, y in coords])

message  = []
for p in range(max_y+1):
    message.append(["."]*(max_x+1))
print(message)

for x, y in coords:
    message[y][x] = "#"
    print(message)
for line in message:
    print("".join(line))