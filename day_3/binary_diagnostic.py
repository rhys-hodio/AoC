import numpy as np

def array_bits_to_int(array):
    l = list(map( lambda x: str(x), list(array)))
    return int("".join(l), 2)


with open('binary.txt') as f:
    lines = f.readlines()
lines = [list(map(lambda x: int(x), list(line.strip()))) for line in lines]

transposed_array = np.transpose(np.array(lines))
transposed_array[transposed_array == 0] = -1
sum_array = np.sum(transposed_array, axis=1)

gamma_array = sum_array.copy()
gamma_array[gamma_array > 0] = 1
gamma_array[gamma_array < 0] = 0
gamma_rate = array_bits_to_int(gamma_array)
epsilon_rate = gamma_rate ^ int("".join(transposed_array.shape[0] * "1"), 2)

ans_1 = gamma_rate * epsilon_rate
print(ans_1)

o2_transpose_array_cpy = transposed_array.copy()
co2_transpose_array_cpy = transposed_array.copy()
for i in range(transposed_array.shape[0]):
    o2_sum = np.sum(o2_transpose_array_cpy[i])
    if o2_sum >= 0:
        o2_drop_idxs = np.where(o2_transpose_array_cpy[i] == -1)
    else:
        o2_drop_idxs = np.where(o2_transpose_array_cpy[i] == 1)
    
    o2_transpose_array_cpy = np.delete(o2_transpose_array_cpy, o2_drop_idxs, 1)
    if o2_transpose_array_cpy.shape[1] == 1:
        break

for i in range(transposed_array.shape[0]):
    co2_sum = np.sum(co2_transpose_array_cpy[i])
    if co2_sum >= 0:
        co2_drop_idxs = np.where(co2_transpose_array_cpy[i] == 1)
    else:
        co2_drop_idxs = np.where(co2_transpose_array_cpy[i] == -1)
    
    co2_transpose_array_cpy = np.delete(co2_transpose_array_cpy, co2_drop_idxs, 1)
    if co2_transpose_array_cpy.shape[1] == 1:
        break

o2_array = np.transpose(o2_transpose_array_cpy).flatten()
o2_array[o2_array == -1] = 0
o2_rate = array_bits_to_int(o2_array)

co2_array = np.transpose(co2_transpose_array_cpy).flatten()
co2_array[co2_array == -1] = 0
co2_rate = array_bits_to_int(co2_array)

ans_2 = o2_rate * co2_rate
print(ans_2)