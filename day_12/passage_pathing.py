import queue
import re

with open("passage.txt") as f:
    lines = f.readlines()

children = {}
for line in lines:
    x, y = re.match(r'(.*)-(.*)', line).groups()
    if x in children and y not in children[x]:
        children[x] += [y]
    else:
        children[x] = [y]
    if y in children  and x not in children[y]:
        children[y] += [x]
    else:
        children[y] = [x]

paths_cnt = 0
for node in children['start']:
    frontier = queue.Queue()
    frontier.put(node)
    print(node)
    while not frontier.empty():
        current = frontier.get()
        print("current=" + current)
        childs = children[current]
        for next in childs:
            print(next)
            if next == 'end':
                paths_cnt += 1
            elif next == 'start' or (current.islower() and next.islower()):
                continue
            else:
                if next.islower() and next in frontier.queue:
                    continue
                else:
                    frontier.put(next)

print(paths_cnt)