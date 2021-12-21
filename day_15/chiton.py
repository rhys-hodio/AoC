import heapq

with open("risk.txt") as f:
    lines = f.readlines()

risks = [list(map(lambda x: int(x), list(line.strip()))) for line in lines]
x_length1 = len(risks[0])
y_length1 = len(risks)

def get_neighbours1(y, x):
    neighbours = []
    if x != 0:
        neighbours.append((y, x-1))
    if x+1 != x_length1:
        neighbours.append((y, x+1))
    if y != 0:
        neighbours.append((y-1, x))
    if y+1 != y_length1:
        neighbours.append((y+1, x))
    return neighbours

frontier = []
start = (0, 0)
goal = (x_length1-1, y_length1-1)
heapq.heappush(frontier, (0, start))
came_from = dict()
cost_so_far = dict()
came_from[start] = None
cost_so_far[start] = 0
while frontier:
    current = heapq.heappop(frontier)[1]
    if current == goal:
        break
    for next in get_neighbours1(current[0], current[1]):
        new_cost = cost_so_far[current] + risks[next[1]][next[0]]
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost
            heapq.heappush(frontier, (priority, next))
            came_from[next] = current

ans_1 = cost_so_far[goal]
print(ans_1)


x_length2 = len(risks[0])*5
y_length2 = len(risks)*5

def get_neighbours2(y, x):
    neighbours = []
    if x != 0:
        neighbours.append((y, x-1))
    if x+1 != x_length2:
        neighbours.append((y, x+1))
    if y != 0:
        neighbours.append((y-1, x))
    if y+1 != y_length2:
        neighbours.append((y+1, x))
    return neighbours

def get_risk(x, y):
    orig_x = x % x_length1
    orig_y = y % y_length1
    mult_x = x // x_length1
    mult_y = y // y_length1
    risk = risks[orig_y][orig_x]
    risk = risk + mult_x + mult_y
    risk -= 1
    risk = risk % 9
    risk += 1
    return risk


frontier = []
start = (0, 0)
goal = (x_length2-1, y_length2-1)
heapq.heappush(frontier, (0, start))
came_from = dict()
cost_so_far = dict()
came_from[start] = None
cost_so_far[start] = 0
while frontier:
    current = heapq.heappop(frontier)[1]
    if current == goal:
        break
    for next in get_neighbours2(current[0], current[1]):
        new_cost = cost_so_far[current] + get_risk(next[0], next[1])
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost
            heapq.heappush(frontier, (priority, next))
            came_from[next] = current

ans_2 = cost_so_far[goal]
print(ans_2)