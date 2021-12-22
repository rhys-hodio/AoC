import math

with open("packets.txt") as f:
    lines = f.readlines()

input_hex = lines[0]
input_bin = bin(int(input_hex, 16))[2:]

def hex_roundup(x):
    x += 1
    return (int(math.ceil(x / 4.0)) * 4) - 1

def literal_packet(start, vcnt):
    end = start
    version = int(input_bin[start:start + 3], 2)
    vcnt += version
    type_id = int(input_bin[start+3:start+3 + 3], 2)
    if type_id != 4:
        raise Exception("lit")
    cnt = 0
    lit_start = start+6
    while True:
        five_bits = input_bin[(lit_start+(cnt*5)):(lit_start+(cnt*5)) + 5]
        end = (lit_start+(cnt*5)) + 5 - 1
        first = int(five_bits[0])
        num = int(five_bits[1:], 2)
        if first == 0:
            break
        cnt += 1
    end = hex_roundup(end)
    
    return vcnt, end

def operator_packet(start, vcnt):
    end = start
    version = int(input_bin[start:start + 3], 2)
    vcnt += version
    type_id = int(input_bin[start+3:start+3 + 3], 2)
    if type_id == 4:
        raise Exception("op")
    length_type = int(input_bin[start+6:start+6 + 1], 2)
    if length_type == 0:
        lpackets = int(input_bin[start+7:start+7 + 15], 2)
        lcnt = 0
        while True
    else:
        npackets = int(input_bin[start+7:start+7 + 11], 2)
    return vcnt, end



type_id = int(input_bin[3:3 + 3], 2)

if type_id == 4:
    version_cnt, end = literal_packet(0, 0)
else:
    version_cnt = operator_packet(0, 0)

ans_1 = version_cnt
print(version_cnt)