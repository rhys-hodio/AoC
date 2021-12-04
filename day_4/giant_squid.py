with open('bingo.txt') as f:
    lines = f.readlines()

def get_chunks(l, n):
      
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]

def remove_num(twod_l, num):
    
    return [[x for x in line if x != num] for line in twod_l]

def check_empty(twod_l):

    for l in twod_l:
        if not l:
            return True
    return False


drawn_numbers = list(map(lambda x: int(x), lines[0].strip().split(",")))
lines = lines[1:]
rows = [list(map(lambda x: int(x), x.strip().split())) for x in lines if x != "\n"]
rows_T = list(map(list, zip(*rows)))
columns = []
for m in rows_T:
    chunks = list(get_chunks(m, 5))
    for chunk in chunks:
        columns.append(chunk)

total_grids = len(rows)//5
assert(len(columns)//5 == total_grids)

grids = {}
for i in range(total_grids):
    grids[i] = rows[i*5:i*5 + 5]
    for j in range(5):
        grids[i].append(columns[i+(j*total_grids)])

grids_cpy1 = grids.copy()

first_grid = None
num_just_called = None
for num in drawn_numbers:
    for key in grids_cpy1.keys():
        grids_cpy1[key] = remove_num(grids_cpy1[key], num)
        if check_empty(grids_cpy1[key]):
            first_grid = grids_cpy1[key]
            num_just_called = num
            break
    if first_grid is not None and num_just_called is not None:
        break


if first_grid is not None and num_just_called is not None:
    grid_sum = sum([sum(i) for i in first_grid]) // 2
    ans_1 = grid_sum * num_just_called
    print(ans_1)


grids_cpy2 = grids.copy()

last_grid = None
num_just_called = None
popped_grids = []
for num in drawn_numbers:
    for key in grids_cpy2.keys():
        grids_cpy2[key] = remove_num(grids_cpy2[key], num)
        if check_empty(grids_cpy2[key]) and key not in popped_grids:
            popped_grids.append(key)
            if len(popped_grids) == total_grids:
                last_grid = grids_cpy2[key]
                num_just_called = num
                break
    if last_grid is not None and num_just_called is not None:
        break
print(grids_cpy2)
if last_grid is not None and num_just_called is not None:
    grid_sum = sum([sum(i) for i in last_grid]) // 2
    ans_2 = grid_sum * num_just_called
    print(ans_2)