'''
借助 PIL 将图片处理成文字

author: fish
date: 2018-2-8
'''
from PIL import Image

# 处理图片的函数
def pic2char(srcPic, savePos):

    '''
将一张图片转换成文字。。。

传入 srcPic 要被转换的图片路径
传入 savePos 要被输出文字的路径

ex:
pic2char("Z:/a.jpg", "Z:/grey.txt")
    '''

    # 先将图片转换为灰度图片
    img = Image.open(srcPic).convert("L")

    # 将图片缩小点，不然文字很长
    img = img.resize((200, 200))

    # 获取宽高，下面开始遍历每个像素，生成相应的字符
    width, height = img.size

    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    length = len(ascii_char)

    text = [] # 存储生成的字符
    for i in range(height):
        for j in range(width):
            grey = img.getpixel((j, i)) # 获得当前像素点的灰度值

            # 根据灰度值来确定生成的字符
            char = ascii_char[int(grey / 256 * length)]
            text.append(char)
        text.append("\n")

    # 将这些字符连成字符串
    text = "".join(text)

    with open(savePos, "w") as f:
        f.write(text)


if __name__ == "__main__":
    pic2char("Z:/code.png", "Z:/grey.txt")
