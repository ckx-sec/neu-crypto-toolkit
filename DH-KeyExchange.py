import random
from Crypto.Util.number import *


def min_g(n):		# 这样默认求最小原根
    k = (n-1)//2
    for i in range(2, n-1):
        if multimod(i, k, n) != 1:
            return i


def multimod(a, k, n):  # 快速幂取模
    ans = 1
    while(k != 0):
        if k % 2:  # 奇数
            ans = (ans % n)*(a % n) % n
        a = (a % n)*(a % n) % n
        k = k//2  # 整除2
    return ans


if __name__ == "__main__":
    p = getPrime(512)
    print("生成的512比特位大质数p为%d" % p)
    g = min_g(p)
    print("最小原根为%d" % g)
    A = random.randint(0, p-1)
    B = random.randint(0, p-1)
    print("A,B各自的随机数分别是%d,%d" % (A, B))
    keyA = pow(g, A, p)
    keyB = pow(g, B, p)
    print("A,B需要交换的密钥分别是%d,%d" % (keyA, keyB))
    S_a = pow(keyB, A, p)
    S_b = pow(keyA, B, p)
    assert(S_a == S_b)
    print("最终交换后产生的共同密钥是%d" % S_a)
