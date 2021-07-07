from typing import Union
from DES_dic import *
from Crypto.Util.number import *
import re

IP_table = [58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7]


IP_re_table = [40, 8, 48, 16, 56, 24, 64, 32, 39,
               7, 47, 15, 55, 23, 63, 31, 38, 6,
               46, 14, 54, 22, 62, 30, 37, 5, 45,
               13, 53, 21, 61, 29, 36, 4, 44, 12,
               52, 20, 60, 28, 35, 3, 43, 11, 51,
               19, 59, 27, 34, 2, 42, 10, 50, 18,
               58, 26, 33, 1, 41, 9, 49, 17, 57, 25]


E = [32, 1,  2,  3,  4,  5,  4,  5,
     6, 7,  8,  9,  8,  9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27,
     28, 29, 28, 29, 30, 31, 32,  1]


P = [16,  7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26,  5, 18, 31, 10,
     2,  8, 24, 14, 32, 27,  3,  9,
     19, 13, 30, 6, 22, 11,  4,  25]


S = [
    [14, 4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
     0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
     4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
     15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13],



    [15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
     3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
     0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
     13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9],


    [10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
     13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
     13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
     1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12],


    [7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11,  12,  4, 15,
     13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14, 9,
     10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
     3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14],


    [2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
     14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
     4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
     11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3],

    [12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
     10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
     9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
     4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13],


    [4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
     13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
     1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
     6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12],


    [13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
     1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
     7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
     2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11],
]


PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10,  2, 59, 51, 43, 35, 27,
        19, 11,  3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14,  6, 61, 53, 45, 37, 29,
        21, 13,  5, 28, 20, 12, 4]


PC_2 = [14, 17, 11, 24,  1,  5,  3, 28,
        15,  6, 21, 10, 23, 19, 12,  4,
        26,  8, 16,  7, 27, 20, 13,  2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]


# 密钥左移的位数
SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def write_file(str_mess):
    try:
        f = open('DES.txt', 'w')
        f.write("{}".format(str_mess))
        f.close()
        print("文件输出成功！")
    except IOError:
        print('文件加解密出错！！！')


def read_file():
    try:
        f = open('DES.txt', 'r')
        mess = f.read()
        f.close()
        print("文件读取成功！")
        return mess
    except IOError:
        print('文件加解密出错！！！')


# IP盒处理
def ip_change(bin_str):
    res = ""
    for i in IP_table:
        res += bin_str[i-1]  # 数组下标i-1
    return res


# IP逆盒处理
def ip_re_change(bin_str):
    res = ""
    for i in IP_re_table:
        res += bin_str[i-1]
    return res

# E盒置换


def e_key(bin_str):
    res = ""
    for i in E:
        res += bin_str[i-1]
    return res


# 字符串异或操作
def str_xor(my_str1, my_str2):
    res = ""
    for i in range(0, len(my_str1)):
        # 变成10进制是转化成字符串 2进制与10进制异或结果一样，都是1,0
        xor_res = int(my_str1[i], 10) ^ int(my_str2[i], 10)
        if xor_res == 1:
            res += '1'
        if xor_res == 0:
            res += '0'

    return res


# 循环左移操作
def left_turn(my_str, num):
    left_res = my_str[num:len(my_str)]
    left_res = my_str[0:num]+left_res
    return left_res


# 密钥的PC-1置换
def change_key1(my_key):
    res = ""
    for i in PC_1:
        res += my_key[i-1]
    return res

# 密钥的PC-2置换


def change_key2(my_key):
    res = ""
    for i in PC_2:
        res += my_key[i-1]
    return res


# S盒过程
def s_box(my_str):
    res = ""
    c = 0
    for i in range(0, len(my_str), 6):
        now_str = my_str[i:i+6]
        row = int(now_str[0]+now_str[5], 2)
        col = int(now_str[1:5], 2)
        # 利用了bin输出有可能不是4位str类型的值，所以才有下面的循环并且加上字符0
        num = bin(S[c][row*16 + col])[2:]
        for gz in range(0, 4-len(num)):
            num = '0' + num
        res += num
        c += 1
    return res


# P盒置换
def p_box(bin_str):
    res = ""
    for i in P:
        res += bin_str[i-1]
    return res


# F函数的实现
def fun_f(bin_str, key):
    first_output = e_key(bin_str)
    second_output = str_xor(first_output, key)
    third_output = s_box(second_output)
    last_output = p_box(third_output)
    return last_output


def gen_key(key):
    key_list = []
    divide_output = change_key1(key)
    key_C0 = divide_output[0:28]
    key_D0 = divide_output[28:]
    for i in SHIFT:
        key_c = left_turn(key_C0, i)
        key_d = left_turn(key_D0, i)
        key_output = change_key2(key_c + key_d)
        key_list.append(key_output)
    return key_list


def encrypt_64bits(bin_message, bin_key):  # 64位二进制加密的测试
    # bin_message = deal_mess(str2bin(message))
    mes_ip_bin = ip_change(bin_message)
    # bin_key = input_key_judge(str2bin(key))
    key_lst = gen_key(bin_key)
    mes_left = mes_ip_bin[0:32]
    mes_right = mes_ip_bin[32:]
    for i in range(0, 15):
        mes_tmp = mes_right
        f_result = fun_f(mes_tmp, key_lst[i])
        mes_right = str_xor(f_result, mes_left)
        mes_left = mes_tmp
    f_result = fun_f(mes_right, key_lst[15])
    mes_fin_left = str_xor(mes_left, f_result)
    mes_fin_right = mes_right
    fin_message = ip_re_change(mes_fin_left + mes_fin_right)
    return fin_message

# 64位二进制解密的测试,注意密钥反过来了，不要写错了


def decrypt_64bits(bin_mess, bin_key):
    mes_ip_bin = ip_change(bin_mess)
    key_lst = gen_key(bin_key)
    lst = range(1, 16)
    cipher_left = mes_ip_bin[0:32]
    cipher_right = mes_ip_bin[32:]
    for i in lst[::-1]:
        mes_tmp = cipher_right
        cipher_right = str_xor(cipher_left, fun_f(cipher_right, key_lst[i]))
        cipher_left = mes_tmp
    fin_left = str_xor(cipher_left, fun_f(cipher_right, key_lst[0]))
    fin_right = cipher_right
    fin_output = fin_left + fin_right
    bin_plain = ip_re_change(fin_output)
    res = long_to_bytes(int(bin_plain, 2))
    return res


def des_encrypt(message: Union[str, bytes], key: Union[str, bytes]) -> str:
    if isinstance(message, str):
        message = message.encode()
    if isinstance(key, str):
        key = key.encode()
    bin_message = "{0:064b}".format(bytes_to_long(message))
    bin_key = "{0:064b}".format(bytes_to_long(key))
    tmp = re.findall(r'.{64}', bin_message)
    res = ""
    for i in tmp:
        res += encrypt_64bits(i, bin_key)
    return res


def des_decrypt(message: str, key: Union[str, bytes]):
    bin_message = "{0:064b}".format(int(message))
    if isinstance(message, bytes):
        message = message.decode()
    if isinstance(key, str):
        key = key.encode()
    bin_key = "{0:064b}".format(bytes_to_long(key))
    res = b""
    tmp = re.findall(r'.{64}', bin_message)
    for i in tmp:
        res += decrypt_64bits(i, bin_key)
    return res


def encrypt_binstr(text: Union[str, bytes], key: Union[str, bytes]) -> str:
    return des_encrypt(text, key)


def decrypt_binstr(text: Union[str, bytes], key: Union[str, bytes]) -> str:
    if isinstance(text, bytes):
        text = text.decode()
    if isinstance(key, str):
        key = key.encode()
    bin_key = "{0:064b}".format(bytes_to_long(key))
    res = b""
    tmp = re.findall(r'.{64}', text)
    for i in tmp:
        res += decrypt_64bits(i, bin_key)
    return res


def get_mode():
    print("1.加密")
    print("2.解密")
    mode = input()
    if mode == '1':
        print("请输入信息输入字符串不能为空：")
        message = input().replace(' ', '')
        print("请输入你的密钥：")
        key = input().replace(' ', '')
        out_mess = int(des_encrypt(message, key), 2)
        print("密文长整型:")
        print(out_mess)
        write_file(out_mess)

    elif mode == '2':
        print("请输入你的密钥：")
        key = input().replace(' ', '')
        message = read_file()
        s = des_decrypt(message, key)
        print("解密后的信息：" + s)
    else:
        print("请重新输入！")


if __name__ == '__main__':
    while True:
        get_mode()
