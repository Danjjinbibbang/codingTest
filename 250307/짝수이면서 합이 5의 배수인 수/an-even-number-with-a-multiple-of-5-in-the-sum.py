n = int(input())

# Please write your code here.
def print_num(n):
    result = "No"
    if(n % 2 == 0 and ((n % 10) + (n//10)) % 5 == 0):
        result = "Yes"
    print(result)

print_num(n)