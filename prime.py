'''
使用生成器写的得到素数模块。。。

primes(num): num 必须给定，默认值是10000

author: fish
date: 2018-2-4
'''
# 产生素数，返回 iterator
def primes(num = 10000):
    def __odd_gen():
        n = 3
        while True:
            yield n
            n = n + 2

    def __div(n):
        return lambda x : x % n > 0
    
    yield 2 # 2 是纯种素数...

    odd_g = __odd_gen()
    while num > 1:
        n = next(odd_g)
        yield n
        odd_g = filter(__div(n), odd_g)
        num -= 1

def main():
    l = list(primes(100))
    for i in l:
        print(i)

if __name__ == "__main__":
    main()
