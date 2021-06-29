from functional import seq


class Caesar:
    @classmethod
    def encode(cls, _text: str, offset: int) -> str:
        text = seq(iter(_text.lower()))
        return text\
            .map(lambda x: ord(x)-97)\
            .map(lambda x: x + offset % 26)\
            .map(lambda x: chr(x+97))\
            .make_string('')
        '''
        return seq(iter(text))\
            .map(lambda c: chr((ord(c)-65-offset) % 26+65))\
            .make_string('')
        '''

    @classmethod
    def decode(cls, _text: str, offset: int) -> str:
        text = seq(iter(_text.lower()))
        return text\
            .map(lambda x: ord(x)-97)\
            .map(lambda x: x - offset % 26)\
            .map(lambda x: chr(x+97))\
            .make_string('')
        '''
        return seq(iter(text))\
            .map(lambda c: chr((ord(c)-65-offset) % 26+65))\
            .make_string('')
        '''

    @classmethod
    def shift(cls, text: str, offset: int) -> str:
        return seq(iter(text))\
            .map(lambda c: chr((ord(c)+offset)))\
            .make_string('')


class Keyword:
    alphabet = seq(list('abcdefghijklmnopqrstuvwxyz'))

    @classmethod
    def encode(cls, _text: str, _keyword: str) -> str:
        keyword = seq(list(_keyword.lower()))
        text = seq(iter(_text.lower()))

        table = cls.alphabet\
            .zip(keyword + cls.alphabet.filter(lambda x: x not in keyword))\
            .dict()
        return text.map(lambda x: table[x]).make_string('')

    @classmethod
    def decode(cls, _text: str, _keyword: str) -> str:
        keyword = seq(list(_keyword.lower()))
        text = seq(iter(_text.lower()))

        table = (keyword + cls.alphabet.filter(lambda x: x not in keyword))\
            .zip(cls.alphabet)\
            .dict()
        return text.map(lambda x: table[x]).make_string('')


class Affine:
    @classmethod
    def encode(cls, _text: str, multi: int, offset: int) -> str:
        text = seq(iter(_text.lower()))
        return text\
            .map(lambda x: ord(x)-97)\
            .map(lambda x: x*multi+offset)\
            .map(lambda x: chr(x % 26+97))\
            .make_string('')

    @classmethod
    def decode(cls, _text: str, multi: int, offset: int) -> str:
        text = seq(iter(_text.lower()))
        table = seq.range(26)\
            .map(lambda x: (
                chr(((x*multi+offset) % 26)+97),
                chr(x+97)
            )).dict()
        return text\
            .map(lambda x: table[x])\
            .make_string('')


class Multiliteral:
    alphabet = seq(list('abcdefghiklmnopqrstuvwxyz'))

    @classmethod
    def encode(cls, _text: str, _key: str) -> str:
        key = seq(list(_key))
        text = seq(iter(_text))
        table = cls.alphabet.zip(
            key.cartesian(key).smap(lambda x, y: x+y)
        ).dict()
        return text.map(lambda x: table[x]).make_string('')

    @classmethod
    def decode(cls, _text: str, _key: str) -> str:
        key = seq(list(_key))
        text = seq(iter(_text))
        table = key.cartesian(key)\
            .smap(lambda x, y: x+y)\
            .zip(cls.alphabet)\
            .dict()
        return text.grouped(2)\
            .smap(lambda x, y: table[x+y])\
            .make_string('')


if __name__ == '__main__':
    assert Caesar.encode('abcdef', 28) == 'cdefgh'
    assert Caesar.decode('cdefgh', 28) == 'abcdef'
    assert Keyword.encode('abcdef', 'cfg') == 'cfgabd'
    assert Keyword.decode('cfgabd', 'cfg') == 'abcdef'
    assert Affine.encode('abcdef', 7, 12) == 'mtahov'
    assert Affine.decode('mtahov', 7, 12) == 'abcdef'
    assert Multiliteral.encode('abcdef', 'btrfs') == 'bbbtbrbfbstb'
    assert Multiliteral.decode('bbbtbrbfbstb', 'btrfs') == 'abcdef'
