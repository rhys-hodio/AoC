with open('ages.txt') as f:
    lines = f.readlines()

ages = list(map(lambda x: int(x), lines[0].split(",")))

def simulate_ages(days):
    results = {}
    lists = {}
    for start_age in [0,1,2,3,4,5,6,7,8]:
        l = [start_age]
        for day in range(days):
            l = list(map(lambda x: x-1, l))
            new_fish = l.count(-1)
            l = [x if x != -1 else 6 for x in l]
            l = l + [8]*new_fish    
        results[start_age] = len(l)
        lists[start_age] = l
    return results, lists


results1, lists1 = simulate_ages(80)
cnt1 = 0
for age in ages:
   cnt1 += results1[age]

ans_1 = cnt1
print(ans_1)

mega_list = []
cnt2 = 0
results2, lists2 = simulate_ages(128)
for age in ages:
   mega_list += lists2[age]
for age in mega_list:
  cnt2 += results2[age]

ans_2 = cnt2
print(ans_2)




