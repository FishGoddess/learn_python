'''
提供文件复制的功能
只需传入 src 源文件路径和 dst 目标文件路径即可

ex:
copy_file("Z:/ser.mp4", "Z:/ser_copy.mp4")

author: fish
date: 2018-2-6
'''

__author__ = "fish"
import time

'''
src: 源文件路径，如 "Z:/ser.mp4"
dst: 目标文件路径，如 "Z:/ser_copy.mp4"
'''
def copy_file(src, dst):
    inp = open(src, "rb")
    oup = open(dst, "wb")
    
    try:
        # 一次性将文件读进内存速度更快，但是更占用内存
        # 文件太大的话有可能导致内存不足
        #oup.write(inp.read())
        while True:
            temp = inp.read(4096)
            if temp == b"":
                break
            oup.write(temp)
    except IOError:
        print("复制失败！")
    finally:
        inp.close()
        oup.close()
        print("Done!")

def main():
    b = time.time()
    copy_file("Z:/ser.mp4", "Z:/ser_copy.mp4")
    e = time.time()

    print("耗时：%.2f 秒！" % (e - b))

if __name__ == "__main__":
    main()
