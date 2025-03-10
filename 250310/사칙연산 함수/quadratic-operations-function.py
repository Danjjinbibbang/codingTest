a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def add(a, c):
    return str(a + c)

def sub(a, c):
    return str(a-c)

def inter(a, c):
    return str(a * c)

def div(a, c):
    return str(a // c)

if(o == '+'):
    print(str(a) + " " + o + " " + str(c) + " = " + add(a, c))
elif(o == '-'):
    print(str(a) + " " + o + " " + str(c) + " = " + sub(a, c))
elif(o == '*'):
    print(str(a) + " " + o + " " + str(c) + " = " + inter(a, c))
elif(o == '/'):
    print(str(a) + " " + o + " " + str(c) + " = " + div(a, c))
else:
    print("False")
