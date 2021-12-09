import queue

with open("heights.txt") as f:
    lines = f.readlines()

heights = list(map(lambda x: list(map(lambda y: int(y), list(x.strip()))), lines))

x_length = len(heights[0])
y_length = len(heights)

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
    return neighbours

low_heights = []
low_heights_coords = []
for y in range(y_length):
    for x in range(x_length):
        low_height = True
        curr_height = heights[y][x]
        neighbours = get_neighbours(y, x)
        for neighbour in neighbours:
            if heights[neighbour[0]][neighbour[1]] <= curr_height:
                low_height = False

        if low_height:
            low_heights.append(curr_height)
            low_heights_coords.append((y, x))

ans_1 = sum(low_heights) + len(low_heights)
print(ans_1)

basin_sizes = []
for coord in low_heights_coords:
    frontier = queue.Queue()
    frontier.put(coord)
    reached = set()
    reached.add(coord)

    while not frontier.empty():
        current = frontier.get()
        neighbours = get_neighbours(current[0], current[1])
        for next in neighbours:
            if next not in reached and heights[next[0]][next[1]] != 9:
                frontier.put(next)
                reached.add(next)
    basin_sizes.append(len(reached))

basin_sizes.sort()
basin_sizes = basin_sizes[::-1]
ans_2 = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
print(ans_2)
        