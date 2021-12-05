import re 

with open('vents.txt') as f:
    lines = f.readlines()

coords = {}

def add_coord(x, y):
    if x in coords:
        if y in coords[x]:
            coords[x][y] += 1
        else:
            coords[x][y] = 1
    else:
        coords[x] = {y: 1}

for line in lines:
    match = re.match(r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)", line)
    x1, y1, x2, y2 = map(lambda x: int(x), match.groups())
    if x1 == x2 and y1 == y2:
        raise Exception("point")
    elif x1 == x2:
        if y1 > y2:
            for i in range(y1 - y2 + 1):
                add_coord(x1, y1-i)
        elif y1 < y2:
            for i in range(y2 - y1 + 1):
                add_coord(x1, y1+i)
    elif y1 == y2:
        if x1 > x2:
            for i in range(x1 - x2 + 1):
                add_coord(x1-i, y1)
        elif x1 < x2:
            for i in range(x2 - x1 + 1):
                add_coord(x1+i, y1)

cnt = 0
for x, y_positions in coords.items():
    for y_position, value in y_positions.items():
        if value >= 2:
            cnt += 1
ans_1 = cnt
print(ans_1)

for line in lines:
    match = re.match(r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)", line)
    x1, y1, x2, y2 = map(lambda x: int(x), match.groups())
   
    if x1 != x2 and y1 != y2:
        if x2 > x1 and y2 > y1:
            coord_l = list(zip(range(x1, x2+1), range(y1, y2+1)))
        elif x2 > x1 and y1 > y2:
            coord_l = list(zip(range(x1, x2+1), range(y1, y2-1, -1)))
        elif x1 > x2 and y2 > y1:
            coord_l = list(zip(range(x1, x2-1, -1), range(y1, y2+1)))
        elif x1 > x2 and y1 > y2:
            coord_l = list(zip(range(x2, x1+1), range(y2, y1+1)))
        for coord in coord_l:
            add_coord(coord[0], coord[1])

cnt = 0
for x, y_positions in coords.items():
    for y_position, value in y_positions.items():
        if value >= 2:
            cnt += 1
ans_2 = cnt
print(ans_2)