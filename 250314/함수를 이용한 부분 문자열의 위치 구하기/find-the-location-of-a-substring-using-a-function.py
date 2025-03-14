text = input()
pattern = input()

# Please write your code here.
def is_match():
    list_text = list(text)
    list_pattern = list(pattern)
    for i in range(len(list_text) - len(list_pattern) + 1):
        if(list_text[i:i+len(list_pattern)] == list_pattern):
            return i
    return -1

print(is_match())
    
