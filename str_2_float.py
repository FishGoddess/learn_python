'''
将一个字符串转化为 float，即使原本不是数字也可以得到一个数字，
所以也可以对一个字符串进行特别加密，至于解密模块还没写。。。

author: fish
date: 2018-2-4
'''

from functools import reduce


# 将 str 转换成 float
def str2float(s):
    
    # 将一个字符串 ls 转化为整数
    def str2int(ls):
        zero_code = ord("0") # 先记录 '0' 的 ASCii值，后面有用

        # 累加每个数为大数
        def fn(x, y):
            return x * 10 + y

        # 将一个字符转化为数字
        def char2num(ch):
            return ord(ch) - zero_code

        return reduce(fn, map(char2num, ls))

    # 将一个字符串转成整数并缩小到 1 以下
    def int2float(ss):
        length = len(ss)
        num = str2int(ss)
        while length > 0:
            num /= 10
            length -= 1
        return num

    nums = s.split(".")
    result = str2int(nums[0]) # 左边大于 1 的部分
    if len(nums) >= 2: # 右边小于 1 的部分
        result = result + int2float(nums[1])
    
    return result

def main():
    print("输入 q 退出！")
    s = None
    while s != "q":
        s = input("请输入一个字符串：")
        print(str2float(s))

if __name__ == "__main__":
    main()
