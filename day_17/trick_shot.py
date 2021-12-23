#target area: x=192..251, y=-89..-59
xmax = 251
xmin = 192
ymax = -59
ymin= -89

y_velocity = abs(ymin) - 1
height = 0
height_l = []
while height not in range(ymin, ymax+1):
    height += y_velocity
    y_velocity -= 1
    height_l.append(height)

ans_1 = max(height_l)
print(ans_1)

step_cnt = 0

x_candidates = {}
x_candidate = 0
while True:
    x_velocity = x_candidate
    x_dist = 0
    steps = 0
    while True:
        steps += 1
        x_dist += x_velocity
        
        if x_dist in range(xmin, xmax+1):
            if x_candidate in x_candidates:
                x_candidates[x_candidate] += [(steps, x_velocity)]
                if x_velocity == 1:
                    x_candidates[x_candidate] += [(steps+1, x_velocity-1)]
            else:
                x_candidates[x_candidate] = [(steps, x_velocity)]
                if x_velocity == 1:
                    x_candidates[x_candidate] += [(steps+1, x_velocity-1)]
        x_velocity = x_velocity - 1 if x_velocity > 0 else 0        
        if x_dist > xmax or x_velocity == 0:
            break
    if x_candidate > xmax:
        break
    x_candidate += 1

xy_candidates = []
for x_cand, step_l in x_candidates.items():
    for steps, vel in step_l:
        y_candidate = ymin
        while True:
            y_velocity = y_candidate
            y_height = 0
            ysteps = 0
            while True:
                ysteps += 1
                y_height += y_velocity
                y_velocity -= 1
                if y_height in range(ymin, ymax+1) and (((ysteps >= steps) and (vel == 0)) or ((ysteps == steps) and (vel != 0))):
                    xy_candidates.append((x_cand, y_candidate))
                    break
                if y_height < ymin:
                    break
            if y_candidate > abs(ymin) - 1:
                break
            y_candidate += 1

ans_2 = len(set(xy_candidates))

print(ans_2)

