'''
使用字典统计物品件数

author: fish
date: 2018-2-7
'''


# 所有宾客带的东西
guests = {"Jack":{"apple":15, "chicken":9},
          "Alice":{"tomato":7, "apple":8},
          "John":{"chicken":12, "drink":11},
          "Kiky":{"drink":4, "bread":17}}


def get_total(things):
    '''
获得所有物品，根据 things 来统计
返回所有物品的字典类型
    '''
    
    total = {}
    for thing in things.values():
        for itemName in thing:
            # 下面这两句也可以实现功能
##            total.setdefault(itemName, 0)
##            total[itemName] += thing[itemName]
            total[itemName] = total.get(itemName, 0) + thing[itemName]

    return total

# 测试
def main():
    total = get_total(guests)
    print(total)

if __name__ == "__main__":
    main()
