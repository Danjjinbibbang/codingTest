secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Code:
    def __init__(self, code, location, time_):
        self.code = code
        self.loc = location
        self.time = time_

code1 = Code(secret_code, meeting_point, time)
print('secret code :', code1.code)
print('meeting point :', code1.loc)
print('time :', code1.time)