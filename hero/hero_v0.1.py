'''
Hero beta-0.1
学习 python 用的小例子

Fish
2018-1-31

'''

print("欢迎来到英雄世界！")
print("| 地图：#####  'a' 向左移动，'d'向右移动|")

hp = 100 # 初始化，游戏角色血量为 100
name = input("请输入角色名：")
if not name:
    name = "玩家一"

usermsg = [name, hp] # 玩家信息

print("您好，！", usermsg[0], "您的血量是：", usermsg[1])
print("您的位置是：*#### |'a' 向左移动，'d'向右移动|")

move = input()
if move == 'a':
    print("您的位置是：*####")
elif move == 'd':
    print("您的位置是：#*###")
