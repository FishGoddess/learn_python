'''
利用递归求汉诺塔：
A B C 三个柱子，先借助 C 将 n - 1 个盘子移动到 B 上，
此时 n - 1 个盘子在 B 上，然后将 A 上的最后一个盘子移动到 C 上，
最后借助 A 将 B 上的 n - 1 个盘子移动到 C 上！

author: Fish
date: 2018-2-4
'''

steps = 0 # 记录移动步数，实际上就等于 2 ^ n - 1 ，n 为盘子个数

# 利用递归求解汉诺塔
def get_moving_steps(n, a, b, c):
    global steps # 声明下面用到的 steps 是上面那个全局变量

    if n == 1:
        steps += 1
        print("第 %d 步：%s --> %s" % (steps, a, c))
    elif n > 1:
        get_moving_steps(n - 1, a, c, b)
        get_moving_steps(1, a, b, c)
        get_moving_steps(n - 1, b, a, c)
def main():
    n = int(input("请输入盘子个数："))
    get_moving_steps(n, "A", "B", "C")
    print("一共移动了 %d 步！" % steps)

if __name__ == "__main__":
    main()
