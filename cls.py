'''
声明和使用类

类名：首字母大写驼峰法
私有属性：__双下划线开头
共有属性：没啥限制

变量：全小写，以下划线隔开
'''

class MyClass(object):
    __private_attr = 0

    def __init__(self, attr):
        self.__private_attr = attr

    
    def set_attr(self, attr):
        self.__private_attr = attr

    
    def get_attr(self):
        return self.__private_attr


def main():
    mc = MyClass(120)
    print(mc.get_attr())
    mc.set_attr(999)
    print(mc.get_attr())

if __name__ == "__main__":
    main()
