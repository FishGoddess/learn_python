import time

'递归求阶乘'
def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)

num = int(input("请输入一个数："))

# 开始时间
begin = time.time()

print("结果是：", fact(num))

# 结束时间
end = time.time()

print("耗时：", end - begin, " s !")
