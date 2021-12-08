import re 

with open('digits.txt') as f:
    lines = f.readlines()

def matches(s1, s2):
    return len(set(s1) & set(s2))

cnt = 0
for line in lines:
    ipt, opt = re.match(r'([a-z ]+) \| ([a-z ]+)', line).groups()
    opt = opt.split(" ")
    for digit in opt:
        if len(digit) in [2, 3, 4, 7]:
            cnt += 1

ans_1 = cnt
print(ans_1)

cnt = 0
for line in lines:
    digit_dict = {}
    opt_digits = ""
    ipt, opt = re.match(r'([a-z ]+) \| ([a-z ]+)', line).groups()
    ipt = ipt.split(" ")
    opt = opt.split(" ")
    for digit in ipt:
        if len(digit) == 2:
            digit_dict["1"] = digit
        elif len(digit) == 3:
            digit_dict["7"] = digit
        elif len(digit) == 4:
            digit_dict["4"] = digit
        elif len(digit) == 7:
            digit_dict["8"] = digit
    for digit in opt:
        if len(digit) == 2:
            opt_digits += "1"
        elif len(digit) == 3:
            opt_digits += "7"
        elif len(digit) == 4:
            opt_digits += "4"
        elif len(digit) == 7:
            opt_digits += "8"
        elif len(digit) == 5: # 2 3 5
            if matches(digit, digit_dict["1"]) == 1 and matches(digit, digit_dict["7"]) == 2 and matches(digit, digit_dict["4"]) == 2:
                opt_digits += "2"
            elif matches(digit, digit_dict["1"]) == 2 and matches(digit, digit_dict["7"]) == 3 and matches(digit, digit_dict["4"]) == 3:
                opt_digits += "3"
            elif matches(digit, digit_dict["1"]) == 1 and matches(digit, digit_dict["7"]) == 2 and matches(digit, digit_dict["4"]) == 3:
                opt_digits += "5"
        elif len(digit) == 6: # 0 6 9 
            if matches(digit, digit_dict["1"]) == 2 and matches(digit, digit_dict["7"]) == 3 and matches(digit, digit_dict["4"]) == 3:
                opt_digits += "0"
            elif matches(digit, digit_dict["1"]) == 1 and matches(digit, digit_dict["7"]) == 2 and matches(digit, digit_dict["4"]) == 3:
                opt_digits += "6"
            elif matches(digit, digit_dict["1"]) == 2 and matches(digit, digit_dict["7"]) == 3 and matches(digit, digit_dict["4"]) == 4:
                opt_digits += "9"
    cnt += int(opt_digits)

ans_2 = cnt
print(ans_2)

