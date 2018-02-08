class A(object):
    def __init__(self):
        print("AAA in")

        # 加了这句话才会执行 B 构造函数。。
        super(A, self).__init__()
        print("AAA out")

class B(object):
    def __init__(self):
        print("BBB in")
        super(B, self).__init__()
        print("BBB out")

class C(A, B):
    def __init__(self):
        print("CCC in")
        super(C, self).__init__()
        print("CCC out")

c = C()
