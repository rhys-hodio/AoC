import queue

with open("energy.txt") as f:
    lines = f.readlines()

levels1 = [list(map(lambda x: int(x), list(line.strip()))) for line in lines]

x_length = len(levels1[0])
y_length = len(levels1)

def get_neighbours(y, x):
    neighbours = []
    if x != 0:
        neighbours.append((y, x-1))
    if x+1 != x_length:
        neighbours.append((y, x+1))
    if y != 0:
        neighbours.append((y-1, x))
    if y+1 != y_length:
        neighbours.append((y+1, x))
    if x != 0 and y != 0:
        neighbours.append((y-1, x-1))
    if x != 0 and (y+1 != y_length):
        neighbours.append((y+1, x-1))
    if y != 0 and (x+1 != x_length):
        neighbours.append((y-1, x+1))
    if (x+1 != x_length) and (y+1 != y_length):
        neighbours.append((y+1, x+1))
    return neighbours

def print_nice(l):
    for p in l:
        x = list(map(lambda x: str(x), p))
        x = ''.join(x)
        print(x)


cnt = 0
for i in range(100):
    flashed = set()
    for y in range(y_length):
        for x in range(x_length):
            levels1[y][x] += 1 
            if levels1[y][x] > 9 and (y,x) not in flashed:
                frontier = queue.Queue()
                frontier.put((y,x))
                flashed.add((y,x))
                while not frontier.empty():
                    current = frontier.get()
                    neighbours = get_neighbours(current[0], current[1])
                    for next in neighbours:
                        levels1[next[0]][next[1]] += 1
                        if levels1[next[0]][next[1]] > 9 and next not in flashed:
                            frontier.put(next)
                            flashed.add(next)
               
   
    for y in range(y_length):
        for x in range(x_length):
             if levels1[y][x] > 9:
                 cnt += 1;
                 levels1[y][x] = 0;
ans_1 = cnt
print(ans_1)

levels2 = [list(map(lambda x: int(x), list(line.strip()))) for line in lines]
step = 1
while True:
    
    cnt = 0
    flashed = set()
    for y in range(y_length):
        for x in range(x_length):
            levels2[y][x] += 1 
            if levels2[y][x] > 9 and (y,x) not in flashed:
                frontier = queue.Queue()
                frontier.put((y,x))
                flashed.add((y,x))
                while not frontier.empty():
                    current = frontier.get()
                    neighbours = get_neighbours(current[0], current[1])
                    for next in neighbours:
                        levels2[next[0]][next[1]] += 1
                        if levels2[next[0]][next[1]] > 9 and next not in flashed:
                            frontier.put(next)
                            flashed.add(next)
               
   
    for y in range(y_length):
        for x in range(x_length):
            if levels2[y][x] > 9:
                cnt += 1;
                levels2[y][x] = 0;
    print_nice(levels2)
    print("_--------")
    if cnt == x_length*y_length:
        break
    else:
        step += 1

ans_2 = step
print(ans_2)


