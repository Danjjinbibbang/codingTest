MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Code:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

codes = []
for i in range(MAX_N):
    codes.append((codenames[i], scores[i]))

# 정렬 key 값을 설정
codes.sort(key=lambda x: x[1])
print(*codes[0]) #*이거 붙이면 tuple에 대해서 unpack해줌