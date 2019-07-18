from PIL import Image
import argparse


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# 首先，构建命令行输入参数处理 ArgumentParser 实例
parser = argparse.ArgumentParser()

# 定义输入文件、输出文件、输出字符画的宽和高
parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高

args = parser.parse_args() # 解析并获取参数
IMG = args.file # 输入的图片文件路径

WIDTH = args.width # 输出字符画的宽度
HEIGHT = args.height # 输出字符画的高度
OUTPUT = args.output # 输出字符画的路径


def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':
    IMG = "exp.png"
    im = Image.open(IMG)
    im = im.convert('RGB')
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt1 = ""
    txt2 = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt1 += get_char(*im.getpixel((j, i)))
        txt1 += '\n'

    Lim = im.convert('L')
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if Lim.getpixel((j,i)) < 180:
                txt2 +="."
            else:
                txt2 +=" "
        txt2 += '\n'
    #字符画输出到文件
    with open("output1.txt",'w') as f:
        f.write(txt1)
    with open("output2.txt", 'w') as f:
        f.write(txt2)
