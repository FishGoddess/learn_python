'''
生成一个 n 位验证码，包含字母和数字
author: Fish
date: 2018-2-2


chr(x): 返回一个 Unicode 编码为 x 的字符
ord(str): 返回 str 字符对应的 Unicode 编码

random 模块中的常用方法：
    random(): 返回 [0, 1) 之间的数，为 float 类型
    randint(a, b): 返回 [a, b] 之间的数，为 int 类型
    choice(seq): 从给定序列 seq 中随机挑一个，通常搭配 range(...) 一起使用

'''
import random


# 生成数字字母列表
def get_letters():
    letters = []

    # 添加数字
    for x in range(10):
        letters.append(chr(ord("0") + x))

    # 添加字母
    for x in range(26):
        code = ord("A") + x
        letters.append(chr(code))
        letters.append(chr(code + 32)) # 小写字母

    return letters


# 字符容器
CONTAINER = get_letters()


# 主要的函数，返回随机生成的 n 位验证码
# mode 为返回值类型，str 表示字符串，list 表示列表
def generate_id_code(n, mode="str"):
    codes = []
    while n:
        codes.append(random.choice(CONTAINER))
        n -= 1

    if mode == "str":
        return "".join(codes)

    return codes


# 测试用的函数
def main():
    print(generate_id_code(4))

# 判断此时是测试还是当作模块被导入
if __name__ == "__main__":
    main()
