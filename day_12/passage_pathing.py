import queue
import re
from  collections import defaultdict

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

def small_cave_cond(path, next):
    cond = False
    d = defaultdict(int)
    for x in path: d[x] += 1
    if next.isupper() or d[next] == 0:
        return cond
    else:
        for key, value in d.items():
            if key.islower() and value >= 2:
                cond = True
        return cond  



paths1 = []
def DFS1(node, path):
    path.append(node)
    childs = children[node]
    for next in childs:
        if next == 'start':
            continue
        elif next == 'end':
            paths1.append(path + ['end'])
        elif next in path and next.islower():
            continue
        else:         
            DFS1(next, path.copy())
paths2 = []
def DFS2(node, path):
    path.append(node)
    childs = children[node]
    for next in childs:
        if next == 'start':
            continue
        elif next == 'end':
            paths2.append(path + ['end'])
        elif small_cave_cond(path.copy(), next):
            continue
        else:         
            DFS2(next, path.copy())



DFS1('start', [])
ans_1 = len(paths1)
print(ans_1)

DFS2('start', [])
ans_2 = len(paths2)
print(ans_2)