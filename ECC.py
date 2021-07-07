import math
import random
from typing import *


def get_inverse(fenmu, p):

    for i in range(1, p):
        if (i*fenmu) % p == 1:
            return i
    return -1


def get_np(x1, y1, x2, y2, a, p):
    """ 
    获取n*p，每次+p，直到求解阶数np=-p 
    """
    flag = 1  # 用于判断斜率k的正负

    # 计算斜率k（当两点相同）
    if x1 == x2 and y1 == y2:
        fenzi = 3 * (x1 ** 2) + a
        fenmu = 2 * y1    # 计算分母

    # 计算斜率k（当两点不同）
    else:
        fenzi = y2 - y1
        fenmu = x2 - x1
        if fenzi * fenmu < 0:
            flag = 0
            fenzi = abs(fenzi)
            fenmu = abs(fenmu)

    # 分子分母约分
    gcd_value = math.gcd(fenzi, fenmu)
    fenzi = fenzi // gcd_value
    fenmu = fenmu // gcd_value

    # 求分母的逆元
    inverse_fenmu = get_inverse(fenmu, p)
    k = (fenzi * inverse_fenmu)

    # 如果斜率k为负
    if flag == 0:
        k = -k
    k = k % p

    # 计算x3,y3 P+Q
    x3 = (k ** 2 - x1 - x2) % p
    y3 = (k * (x1 - x3) - y1) % p
    return x3, y3


def get_rank(x0, y0, a, b, p):
    """ 
    计算椭圆曲线的阶 
    """
    x1 = x0  # -p的x坐标
    y1 = (-1*y0) % p  # -p的y坐标
    temp_x = x0
    temp_y = y0
    n = 1
    while True:
        n += 1
        # 递归加（选择使用加法，较为简单）
        p_x, p_y = get_np(temp_x, temp_y, x0, y0, a, p)

        # 如果 == -p,那么阶数+1，结束
        if p_x == x1 and p_y == y1:
            return n+1
        temp_x = p_x
        temp_y = p_y


def get_param(x0, a, b, p):
    """ 
    计算p与-p 
    """
    y0 = -1
    for i in range(p):
        # 查看椭圆曲线上是否存在x为该值的点
        if pow(i, 2, p) == (x0**3 + a*x0 + b) % p:
            y0 = i
            break
        # 没有时
    if y0 == -1:
        return False

    # 有p(x0,y0),计算-p(x1,y1)
    x1 = x0
    y1 = (-1*y0) % p
    return x0, y0, x1, y1


def get_graph(a, b, p) -> List[List[int]]:
    """ 
    输出椭圆曲线散点图\n
    返回list[column][row]
    """
    x_y = []
    # 初始化二维数组
    for i in range(p):
        x_y.append(['-' for i in range(p)])

    for i in range(p):
        val = get_param(i, a, b, p)  # 椭圆曲线上的点
        if(val != False):
            x0, y0, x1, y1 = val
            x_y[x0][y0] = 1
            x_y[x1][y1] = 1

    print("椭圆曲线的散列图为：")
    for i in range(p):              # i= 0-> p-1
        temp = p-1-i        # 倒序

        # 格式化输出1/2位数，y坐标轴
        if temp >= 10:
            print(temp, end=" ")
        else:
            print(temp, end="  ")

        # 输出具体坐标的值，一行
        for j in range(p):
            print(x_y[j][temp], end="  ")
        print("")  # 换行

    # 输出 x 坐标轴
    print("  ", end="")
    for i in range(p):
        if i >= 10:
            print(i, end=" ")
        else:
            print(i, end="  ")
    print('\n')

    return x_y


def get_kG(x, y, privatekey, a, p):
    """ 
    计算nG 
    """
    temp_x = x
    temp_y = y
    while privatekey != 1:
        # k次相加得K=kG,输出坐标
        temp_x, temp_y = get_np(temp_x, temp_y, x, y, a, p)
        privatekey -= 1
    return temp_x, temp_y


def ecc_main():
    while True:
        a = int(input("请输入椭圆曲线参数a："))
        b = int(input("请输入椭圆曲线参数b："))
        p = int(input("请输入椭圆曲线参数p(p为素数)："))

        # 条件判断
        if (4*(a**3)+27*(b**2)) % p == 0:
            print("参数有误，请重新输入\n")
        else:
            break

    # 输出椭圆曲线散点图
    get_graph(a, b, p)

    # 选点作为G点
    print("在如上坐标系中选一个值为G的坐标")
    G_x = int(input("user1：请输入选取的x坐标值："))
    G_y = int(input("user1：请输入选取的y坐标值："))

    # 获取椭圆曲线的阶
    n = get_rank(G_x, G_y, a, b, p)

    # user1生成私钥k
    key = int(input("user1：请输入私钥小key（<{}）：".format(n)))

    # user1生成公钥K
    K_x, K_y = get_kG(G_x, G_y, key, a, p)

    # user2拿到user1的公钥K，Ep(a,b)阶n，加密需要加密的明文数据
    # 加密准备
    r = int(input("user2：请输入一个整数r（<{}）用于求rG和rK：".format(n)))
    rG_x, rG_y = get_kG(G_x, G_y, r, a, p)
    rK_x, rK_y = get_kG(K_x, K_y, r, a, p)

    # 加密
    plain_text = input("user2：请输入需要加密的字符串:")
    plain_text = plain_text.strip().encode()
    c = []
    print("密文为：", end="")
    for i in plain_text:
        num = i
        cipher_text = num*rK_x
        c.append([rG_x, rG_y, cipher_text])
        print("(({},{}),{})".format(rG_x, rG_y, cipher_text), end=" ")

    # user1 知道 kG_x,kG_y，key，求解kQ_x,kQ_y，plain_text = cipher_text/kQ_x
    print("\nuser1解密得到明文：", end="")
    d = bytearray()
    for i in c:
        decrypto_text_x, decrypto_text_y = get_kG(
            i[0], i[1], key, a, p)
        d.append(i[2]//decrypto_text_x)
        #print(chr(i[2]//decrypto_text_x), end="")
    print(d.decode())


def decrypt(text, k, a, p):
    ret = bytearray()
    for i in text:
        decrypto_text_x, decrypto_text_y = get_kG(
            i[0][0], i[0][1], k, a, p)
        ret.append(i[1]//decrypto_text_x)
    return bytes(ret)


def encrypt(text, K_x, K_y, G_x, G_y, a, p, n, k):
    rs = [i for i in range(n)]
    rs.remove(k)
    r = random.choice(rs)
    c = []
    rG_x, rG_y = get_kG(G_x, G_y, r, a, p)
    rK_x, rK_y = get_kG(K_x, K_y, r, a, p)

    for i in text:
        num = i
        cipher_text = num*rK_x
        c.append([(rG_x, rG_y), cipher_text])
    return c


if __name__ == "__main__":
    ecc_main()
