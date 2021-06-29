from functional import seq
from itertools import cycle


vigenere_table = ['abcdefghijklmnopqrstuvwxyz',
                  'bcdefghijklmnopqrstuvwxyza',
                  'cdefghijklmnopqrstuvwxyzab',
                  'defghijklmnopqrstuvwxyzabc',
                  'efghijklmnopqrstuvwxyzabcd',
                  'fghijklmnopqrstuvwxyzabcde',
                  'ghijklmnopqrstuvwxyzabcdef',
                  'hijklmnopqrstuvwxyzabcdefg',
                  'ijklmnopqrstuvwxyzabcdefgh',
                  'jklmnopqrstuvwxyzabcdefghi',
                  'klmnopqrstuvwxyzabcdefghij',
                  'lmnopqrstuvwxyzabcdefghijk',
                  'mnopqrstuvwxyzabcdefghijkl',
                  'nopqrstuvwxyzabcdefghijklm',
                  'opqrstuvwxyzabcdefghijklmn',
                  'pqrstuvwxyzabcdefghijklmno',
                  'qrstuvwxyzabcdefghijklmnop',
                  'rstuvwxyzabcdefghijklmnopq',
                  'stuvwxyzabcdefghijklmnopqr',
                  'tuvwxyzabcdefghijklmnopqrs',
                  'uvwxyzabcdefghijklmnopqrst',
                  'vwxyzabcdefghijklmnopqrstu',
                  'wxyzabcdefghijklmnopqrstuv',
                  'xyzabcdefghijklmnopqrstuvw',
                  'yzabcdefghijklmnopqrstuvwx',
                  'zabcdefghijklmnopqrstuvwxy']


class Vigenere:

    @classmethod
    def encode(cls, _text: str, _key: str) -> str:
        text = seq(list(_text.lower())).map(lambda x: ord(x)-97)
        key = seq(cycle(_key.lower())).map(lambda x: ord(x)-97)
        return text\
            .zip(key)\
            .smap(lambda x, y: vigenere_table[y][x])\
            .make_string('')

    @classmethod
    def decode(cls, _text: str, _key: str) -> str:
        text = seq(list(_text.lower())).map(lambda x: ord(x)-97)
        key = seq(cycle(_key.lower())).map(lambda x: ord(x)-97)
        return text\
            .zip(key)\
            .smap(lambda x, y: vigenere_table[y].find(chr(x+97)))\
            .map(lambda x: vigenere_table[0][x])\
            .make_string('')


class AutokeyCipher:
    @classmethod
    def encode(cls, _text: str, _key: str) -> str:
        key = list(_key.lower())
        text = _text.lower()
        for i in range(len(text)):
            key.append(vigenere_table[ord(key[i])-97][ord(text[i])-97])
        return ''.join(key[len(_key):])

    @classmethod
    def decode(cls, _text: str, _key: str) -> str:
        text = seq(list(_text.lower())).map(lambda x: ord(x)-97)
        key = seq(list(_key.lower())).map(lambda x: ord(x)-97) + text
        return text\
            .zip(key)\
            .smap(lambda x, y: vigenere_table[y].find(chr(x+97)))\
            .map(lambda x: vigenere_table[0][x])\
            .make_string('')

    # 下面这段代码能用！
    # ...就是写的有点恶心
    # by nyonsama
    '''
    @classmethod
    def fencode(cls, _text: str, _key: str) -> str:
        text = seq(list(_text.lower())).map(lambda x: ord(x)-97)
        key = seq(list(_key.lower())).map(lambda x: ord(x)-97)

        def inner(text, key):
            if text.empty():
                return key
            return key + inner(
                text.drop(len(_key)),
                key.zip(text).smap(lambda x, y: ord(vigenere_table[x][y])-97))

        return inner(text, key)\
            .drop(len(_key))\
            .map(lambda x: chr(x+97))\
            .make_string('')
    '''


class AutokeyPlain:
    @classmethod
    def encode(cls, _text: str, _key: str) -> str:
        text = seq(list(_text.lower())).map(lambda x: ord(x)-97)
        key = seq(list(_key.lower())).map(lambda x: ord(x)-97) + text
        return text\
            .zip(key)\
            .smap(lambda x, y: vigenere_table[y][x])\
            .make_string('')

    @classmethod
    def decode(cls, _text: str, _key: str) -> str:
        key = list(_key.lower())
        text = _text.lower()
        for i in range(len(text)):
            column = vigenere_table[ord(key[i])-97].find(text[i])
            key.append(vigenere_table[0][column])
        return ''.join(key[len(_key):])


if __name__ == '__main__':
    assert Vigenere.encode('abcdef', 'amr') == 'antdqw'
    assert Vigenere.decode('antdqw', 'amr') == 'abcdef'
    assert AutokeyCipher.encode('ihopethisworks', 'alice') == 'iswribzejepqob'
    assert AutokeyCipher.decode('iswribzejepqob', 'alice') == 'ihopethisworks'
    assert AutokeyPlain.encode('ihopethisworks', 'alice') == 'iswribowhahysk'
    assert AutokeyPlain.decode('iswribowhahysk', 'alice') == 'ihopethisworks'
