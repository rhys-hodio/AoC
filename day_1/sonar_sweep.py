with open('input.txt') as f:
    lines = f.readlines()

depths = list(map(lambda x: int(x), lines))
inc_cnt = 0
for i in range(len(depths) - 1):
    if depths[i+1] > depths[i]:
        inc_cnt += 1

ans_1 = inc_cnt
print(ans_1)

inc_cnt = 0
for i in range(len(depths) - 3):
    if depths[i+3] > depths[i]:
        inc_cnt += 1

ans_2 = inc_cnt
print(ans_2)
  