import re
from  collections import defaultdict

with open("polymer.txt") as f:
    lines = f.readlines()

chain = list(lines[0].strip())


insertions = {}
for line in lines[2:]:
    pair, insert = re.match(r'([A-Z]+) -> ([A-Z])', line.strip()).groups()
    insertions[pair] = insert

chain1 = chain.copy()
for step in range(10):
    post_insert = {}
    for i in range(len(chain1) - 1):
        pair = chain1[i] + chain1[i+1]
        if pair in insertions:
            post_insert[i+1] = insertions[pair]
    ordered_keys = sorted(post_insert.keys())
    num_insertions = 0
    for key in ordered_keys:
        value = post_insert[key]
        chain1.insert(key+num_insertions, value)
        num_insertions += 1


d = defaultdict(int)
for x in chain1: d[x] += 1
ans_1 = max(d.values()) - min(d.values())
print(ans_1)

chain2 = chain.copy()
for step in range(40):
    post_insert = {}
    for i in range(len(chain2) - 1):
        pair = chain2[i] + chain2[i+1]
        if pair in insertions:
            post_insert[i+1] = insertions[pair]
    ordered_keys = sorted(post_insert.keys())
    num_insertions = 0
    for key in ordered_keys:
        value = post_insert[key]
        chain2.insert(key+num_insertions, value)
        num_insertions += 1


d = defaultdict(int)
for x in chain2: d[x] += 1
ans_2 = max(d.values()) - min(d.values())
print(ans_2)