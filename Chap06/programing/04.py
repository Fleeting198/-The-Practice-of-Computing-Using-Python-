# -*- coding:utf-8 -*-
""" 破解密码 """

def encode(plane, shift):
    """ 凯撒加密，输入明文和偏移量 """
    plane = plane.upper()
    cipher = ''.join(
        [chr((ord(char) - 65 + int(shift)) % 26 + 65) if 65 <= ord(char) <= 90 else char for char in plane])
    # for char in plane:
    #     if 65 <= ord(char) <= 90:
    #         cipher.append(chr((ord(char) - 65 + int(shift)) % 26 + 65))
    #     else:
    #         cipher.append(char)
    # cipher = ''.join(cipher)

    return cipher


def decode(cipher, shift):
    """ 凯撒加密，输入密文和偏移量，是加密的逆操作 """
    return encode(cipher, -int(shift))


def find_shift(cipher):
    """ 将出现频率最高的字符当作为 'e'，以此推测偏移量 """
    list_count = [0 for i in range(26)]
    for char in cipher:
        if 65 <= ord(char) <= 90:
            list_count[ord(char) - 65] += 1

    maxv = max(list_count)
    shift = 0
    for i in range(26):
        if list_count[i] == maxv:
            shift = i + 65 - 69

    return shift


def auto_decode(cipher):
    """ 推测偏移量解密文 """
    return decode(cipher, find_shift(cipher))


if __name__ == '__main__':
    shift = 0
    plane = ''
    while 1:
        try:
            shift = int(input('请输入偏移量：'))
            plane = input('请输入明文：')
        except ValueError:
            print('输入有误：应输入整数。')
        else:
            print()
            break

    cipher = encode(plane, shift)
    plane_direct = decode(cipher, shift)
    plane_infer = auto_decode(cipher)

    print('明文：', plane)
    print('密文：', cipher)
    print('直接解密后得到的明文：', plane_direct)
    print('推测解密后得到的明文（可能错误）：', plane_infer)
