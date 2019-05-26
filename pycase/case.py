# -*- coding: utf-8 -*-

# @Date    : 2019-05-26
# @Author  : Peng Shiyu

import argparse


def convert_upper(text):
    text = text.title()
    return text.replace("_", "")


def convert_lower(text):
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)

    return "".join(lst).lower()


def main():
    parser = argparse.ArgumentParser()

    # 可选参数
    parser.add_argument("-f", help="强制转换成小写:lower, 大写: upper")

    # 位置参数
    parser.add_argument("text", help="要转换的字符串")

    # 解析
    args = parser.parse_args()

    text = args.text
    convert = args.f

    if convert is None:
        if "_" in text:
            convert = "upper"
        else:
            convert = "lower"

    if convert == "upper":
        print(convert_upper(text))

    elif convert == "lower":
        print(convert_lower(text))

    else:
        print("参数不正确，-h 查看帮助")


if __name__ == '__main__':
    main()
