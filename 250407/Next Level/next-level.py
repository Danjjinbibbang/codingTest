user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class User:
    def __init__(self, user_id, user_level):
        self.user_id = user_id
        self.user_level = user_level

user1 = User('codetree', '10')
user2 = User(user2_id, user2_level)

print('user', user1.user_id, 'lv', user1.user_level)
print('user', user2.user_id, 'lv', user2.user_level)