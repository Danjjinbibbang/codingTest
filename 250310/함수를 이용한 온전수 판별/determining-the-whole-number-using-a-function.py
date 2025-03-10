a, b = map(int, input().split())

# Please write your code here.
def search_num(n):
    if(n % 2 == 0):
        return False
    if((n >= 10 and n % 10 == 5) or n==5):
        return False
    if(n % 3 == 0 and n % 9 != 0):
        return False
    return True

def cnt_num(a, b):
    count = 0
    for i in range(a, b+1):
        if(search_num(i)):
            count += 1
    print(count)
cnt_num(a, b)
