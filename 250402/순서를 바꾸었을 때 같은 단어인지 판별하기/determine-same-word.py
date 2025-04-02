word1 = input()
word2 = input()

# Please write your code here.
list_word1 = sorted(word1)
list_word2 = sorted(word2)

def str_match(word1, word2):
    flag = True
    if(len(word1) != len(word2)):
        return False

    for i in range(len(word1)):
        if(word1[i] != word2[i]):
            return False
    return flag

if(not str_match(list_word1, list_word2)):
    print("No")
else:
    print("Yes")