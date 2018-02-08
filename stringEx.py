'''
判断一串字母能不能拼出 friend 这个字符串
'''
s = input("请输入一串英文：")

friend = [] # 统计每个字符个数
for i in range(6):
    friend.append(s.count("friend"[i]))

count = min(friend)

# 这里 count != 0 貌似有些繁琐？
while count:
    print("friend")
    count -= 1
    
print("能组成", min(friend), "个 friend")
