import random
import math
from typing import Tuple
from Crypto.Util.number import long_to_bytes, bytes_to_long


def miller_rabin(p):
    if p == 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    m, k, = p - 1, 0
    while m % 2 == 0:
        m, k = m // 2, k + 1
    a = random.randint(2, p - 1)
    x = pow(a, m, p)
    if x == 1 or x == p - 1:
        return True
    while k > 1:
        x = pow(x, 2, p)
        if x == 1:
            return False
        if x == p - 1:
            return True
        k = k - 1
    return False


# 生成大素数
def getPrime(n, r=40):
    while(1):
        p = random.getrandbits(n)
        for _ in range(r):
            if miller_rabin(p) == False:
                pass
            else:
                return p


# 扩展欧几里得算法求模逆
def inverse(e, phi):
    if math.gcd(e, phi) != 1:
        return None
    u1, u2, u3 = 1, 0, e
    v1, v2, v3 = 0, 1, phi
    while v3 != 0:
        q = u3//v3
        v1, v2, v3, u1, u2, u3 = (u1-q*v1), (u2-q*v2), (u3-q*v3), v1, v2, v3
    return u1 % phi


def encrypt(m: bytes, n: int, e: int = 65537) -> int:
    '''m:明文 n:公钥 e:参数e'''
    m = bytes_to_long(m)
    return pow(m, e, n)


def decrypt(c: int, d: int, n: int) -> bytes:
    '''c:密文 d:私钥 n:公钥'''
    return long_to_bytes(pow(c, d, n))


def keygen(e: int = 65537) -> Tuple[int, int]:
    '''返回(公钥，私钥)'''
    if not e:
        e = 65537
    p = getPrime(256)
    q = getPrime(256)
    n = p*q
    phi = (p-1)*(q-1)
    d = inverse(e, phi)
    return (n, d)


if __name__ == '__main__':
    message = b"this is message"
    m = bytes_to_long(message)  # 明文
    p = getPrime(512)
    q = getPrime(512)
    n = p*q  # 公钥
    phi = (p-1)*(q-1)
    e = 65537  # e
    d = inverse(e, phi)  # 私钥

    c = pow(m, e, n)  # 密文
    m_de = pow(c, d, n)  # 解密
    de = long_to_bytes(m_de)
    print(c)
    print(de)
