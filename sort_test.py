# coding=UTF8
import time
import random

begin = time.time()
l = []
r = range(5000000)
for i in r:
    l.append(random.choice(r))
end = time.time()

print("数组生成耗时：%.2f s" % (end - begin))

begin = time.time()
l.sort()
end = time.time()

print("500万个元素排序耗时：%.2f s" % (end - begin))
