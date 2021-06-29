from Crypto.Util.number import *

message = b"this is message"
m = bytes_to_long(message)
p = getPrime(512)
q = getPrime(512)
n = p*q
phi = (p-1)*(q-1)
e = 65537
d = inverse(e, phi)
c = pow(m, e, n)
m_de = pow(c, d, n)
de = long_to_bytes(m_de)
print(c)
print(de)
