import queue

with open("syntax.txt") as f:
    lines = f.readlines()

char_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
char_score_2 = {"(": 1, "[": 2, "{": 3, "<": 4}

lines = [list(line.strip()) for line in lines]
illegal_characters = []
incomplete_lines = []
for line in lines:
    q = queue.LifoQueue()
    illegal = False
    for char in line:
        if char in ["(", "[", "{", "<"]:
            q.put(char)
        elif char in [")", "]", "}", ">"]:
            if q.qsize() > 0:
                char_q = q.get()
                if char_q+char not in ["()", "[]", "{}", "<>"]:
                    illegal_characters.append(char)
                    illegal = True
                    break
            else:
                illegal_characters.append(char)
                illegal = True
                break
        else:
            raise Exception("unexpected char: %s" % char)
    if not illegal:
        incomplete_lines.append(list(q.queue))

score = 0
for char in illegal_characters:
    score += char_score[char]

ans_1 = score
print(ans_1)

scores = []
for line in incomplete_lines:
    line = line[::-1]
    score = 0
    for char in line:
        score *= 5
        score += char_score_2[char]
    scores.append(score)

scores.sort()
ans_2 = scores[len(scores)//2]
print(ans_2)
