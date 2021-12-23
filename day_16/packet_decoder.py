from functools import reduce

with open("packets.txt") as f:
    lines = f.readlines()

input_hex = lines[0]
input_bin = (bin(int(input_hex, 16))[2:]).zfill(len(input_hex)*4)

def literal_packet(start, vcnt):
    end = start
    version = int(input_bin[start:start + 3], 2)
    vcnt += version
    type_id = int(input_bin[start+3:start+3 + 3], 2)
    if type_id != 4:
        raise Exception("lit")
    cnt = 0
    lit_start = start+6
    val = ''
    while True:
        five_bits = input_bin[(lit_start+(cnt*5)):(lit_start+(cnt*5)) + 5]
        end = (lit_start+(cnt*5)) + 5 - 1
        first = int(five_bits[0])
        val += five_bits[1:]
        if first == 0:
            break
        cnt += 1
    val = int(val, 2)
    return vcnt, end, val

def operator_packet(start, vcnt):
    end = start
    operator_values = []
    version = int(input_bin[start:start + 3], 2)
    vcnt += version
    type_id = int(input_bin[start+3:start+3 + 3], 2)
    length_type = int(input_bin[start+6:start+6 + 1], 2)
    if length_type == 0:
        lpackets = int(input_bin[start+7:start+7 + 15], 2)
        lcnt = 0
        sub_packet_start = start + 22
        while True:
            sub_packet_type_id = int(input_bin[sub_packet_start+3:sub_packet_start+3 + 3], 2)
            if sub_packet_type_id == 4:
                vcnt, end, val = literal_packet(sub_packet_start, vcnt)
                operator_values.append(val)
            else:
                vcnt, end, val = operator_packet(sub_packet_start, vcnt)
                operator_values.append(val)
            lcnt += (end - sub_packet_start + 1)
            if lcnt == lpackets:
                break
            else:
                sub_packet_start = end + 1
            
    else:
        npackets = int(input_bin[start+7:start+7 + 11], 2)
        sub_packet_start = start + 18
        for i in range(npackets):
            sub_packet_type_id = int(input_bin[sub_packet_start+3:sub_packet_start+3 + 3], 2)
            if sub_packet_type_id == 4:
                vcnt, end, val = literal_packet(sub_packet_start, vcnt)
                operator_values.append(val)
            else:
                vcnt, end, val = operator_packet(sub_packet_start, vcnt)
                operator_values.append(val)
            sub_packet_start = end + 1
    
    if type_id == 0:
        val = sum(operator_values)
    elif type_id == 1:
        val = reduce((lambda x, y: x * y), operator_values)
    elif type_id == 2:
        val = min(operator_values)
    elif type_id == 3:
        val = max(operator_values)
    elif type_id == 4:
        raise Exception("op4") 
    elif type_id == 5:
        if len(operator_values) != 2:
            raise Exception("op5")
        else:
            val = 1 if operator_values[0] > operator_values[1] else 0
    elif type_id == 6:
        if len(operator_values) != 2:
            raise Exception("op6")
        else:
            val = 1 if operator_values[0] < operator_values[1] else 0
    elif type_id == 7:
        if len(operator_values) != 2:
            raise Exception("op7")
        else:
            val = 1 if operator_values[0] == operator_values[1] else 0
    else:
        raise Exception("op_out_of_bounds") 
             
    return vcnt, end, val



type_id = int(input_bin[3:3 + 3], 2)

if type_id == 4:
    version_cnt, end, val = literal_packet(0, 0)
else:
    version_cnt, end, val = operator_packet(0, 0)

ans_1 = version_cnt
print(version_cnt)

ans_2 = val
print(val)