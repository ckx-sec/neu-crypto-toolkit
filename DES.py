from DES_dic import *
from Crypto.Util.number import *
import re


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


# 秘钥的PC-1置换
def change_key1(my_key):
    res = ""
    for i in PC_1:
        res += my_key[i-1]
    return res

# 秘钥的PC-2置换


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
    #bin_message = deal_mess(str2bin(message))
    mes_ip_bin = ip_change(bin_message)
    #bin_key = input_key_judge(str2bin(key))
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

# 64位二进制解密的测试,注意秘钥反过来了，不要写错了


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
    res = str(long_to_bytes(int(bin_plain, 2)), encoding="utf-8")
    return res


def des_encrypt(message, key):
    message = bytes(message, encoding="utf8")
    message = bytes_to_long(message)
    bin_message = "{0:064b}".format(message)
    key = bytes(key, encoding="utf8")
    key = bytes_to_long(key)
    bin_key = "{0:064b}".format(key)
    tmp = re.findall(r'.{64}', bin_message)
    res = ""
    for i in tmp:
        res += encrypt_64bits(i, bin_key)
    return res


def des_decrypt(message, key):
    bin_message = "{0:064b}".format(int(message))
    key = bytes(key, encoding="utf8")
    key = bytes_to_long(key)
    bin_key = "{0:064b}".format(key)

    res = ""
    tmp = re.findall(r'.{64}', bin_message)
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
        print("请输入你的秘钥：")
        key = input().replace(' ', '')
        s = des_encrypt(message, key)
        out_mess = int(s, 2)
        print("密文长整型:")
        print(out_mess)
        write_file(out_mess)

    elif mode == '2':
        # print("请输入信息输入字符串不能为空：")
        # message = input().replace(' ', '')
        print("请输入你的秘钥：")
        key = input().replace(' ', '')
        message = read_file()
        s = des_decrypt(message, key)
        #out_mess = bin2str(s)
        print("解密后的信息：" + s)
    else:
        print("请重新输入！")


if __name__ == '__main__':
    while True:
        get_mode()
