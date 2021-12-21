import re
from  collections import defaultdict

with open("polymer.txt") as f:
    lines = f.readlines()

chain = list(lines[0].strip())
chain_pairs = [''.join(p) for p in zip(chain, chain[1:])]
missed_letter = chain[-1]

insertions = {}
for line in lines[2:]:
    pair, insert = re.match(r'([A-Z]+) -> ([A-Z])', line.strip()).groups()
    insertions[pair] = insert

d_cnt = defaultdict(int)
for x in chain_pairs: d_cnt[x] += 1
for step in range(10):
    d_cnt_new = {key: 0 for key in insertions.keys()}
    for key, value in d_cnt.items():
        insert = insertions[key]
        d_cnt_new[key[0]+insert] += value
        d_cnt_new[insert+key[1]] += value
    d_cnt = d_cnt_new

letter_cnt = defaultdict(int)
for key, value in d_cnt.items(): letter_cnt[key[0]] += value
letter_cnt[missed_letter] += 1
ans_1 = max(letter_cnt.values()) - min(letter_cnt.values())
print(ans_1)

d_cnt = defaultdict(int)
for x in chain_pairs: d_cnt[x] += 1
for step in range(40):
    d_cnt_new = {key: 0 for key in insertions.keys()}
    for key, value in d_cnt.items():
        insert = insertions[key]
        d_cnt_new[key[0]+insert] += value
        d_cnt_new[insert+key[1]] += value
    d_cnt = d_cnt_new

letter_cnt = defaultdict(int)
for key, value in d_cnt.items(): letter_cnt[key[0]] += value
letter_cnt[missed_letter] += 1
ans_2 = max(letter_cnt.values()) - min(letter_cnt.values())
print(ans_2)