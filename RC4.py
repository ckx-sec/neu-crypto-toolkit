from typing import Union


def _init_box(key):
    s_box = list(range(256))
    j = 0
    for i in range(256):
        #j = (j + s_box[i] + ord(key[i % len(key)])) % 256
        j = (j + s_box[i] + key[i % len(key)]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    return s_box


def encrypt(plain: bytes, key: Union[str, bytes]) -> bytes:
    if isinstance(key, str):
        key = key.encode()
    box = _init_box(key)
    res = bytearray()
    i = j = 0
    for s in plain:
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        box[i], box[j] = box[j], box[i]
        t = (box[i] + box[j]) % 256
        k = box[t]
        res.append(s ^ k)
    return bytes(res)


def decrypt(plain: bytes, key: Union[str, bytes]) -> bytes:
    return encrypt(plain, key)


if __name__ == '__main__':
    assert encrypt(b'asdfghjk', 'polkit') == b'-V\x89g\xc8{\xff\xfa'
