'''
测试 python 各种字符串连接的速度

author: fish
date: 2018-2-8
'''
import time


# 两种测试数据：
# 一个是不同的字符，一个是相同的字符
diff_many_chars = tuple(str(i) for i in range(1000000))
diff_less_chars = tuple(str(i) for i in range(10))
same_many_chars = tuple("666" for i in range(1000000))
same_less_chars = tuple("666" for i in range(10))

# 测试的函数
def test(name, func, text):
    begin = time.time()
    s = func(text)
    end = time.time()

    print("%s 耗时：%.4f 秒！" % (name, end - begin))
    return s

# s = s + "..."
def str_add(text):
    s = ""
    for i in text:
        s += i
    return s

# "".join(list)
def str_join(text):
    temp = []
    for i in text:
        temp.append(i)
    s = "".join(temp)
    return s

if __name__ == "__main__":
    print("%d 个不同数据进行拼接：" % len(diff_many_chars))
    s1 = test("s = s + \"...\"", str_add, diff_many_chars)
    s2 = test("\"\".join(list)", str_join, diff_many_chars)
    print("%d ( 1 表示两种拼接的结果一样) \n " % len({s1, s2}))

    print("%d 个相同数据进行拼接：" % len(same_many_chars))
    s1 = test("s = s + \"...\"", str_add, same_many_chars)
    s2 = test("\"\".join(list)", str_join, same_many_chars)
    print("%d ( 1 表示两种拼接的结果一样) \n " % len({s1, s2}))

    print("%d 个不同数据进行拼接：" % len(diff_less_chars))
    s1 = test("s = s + \"...\"", str_add, diff_less_chars)
    s2 = test("\"\".join(list)", str_join, diff_less_chars)
    print("%d ( 1 表示两种拼接的结果一样) \n " % len({s1, s2}))

    print("%d 个相同数据进行拼接：" % len(same_less_chars))
    s1 = test("s = s + \"...\"", str_add, same_less_chars)
    s2 = test("\"\".join(list)", str_join, same_less_chars)
    print("%d ( 1 表示两种拼接的结果一样) \n " % len({s1, s2}))
