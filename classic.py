from typing import List
from itertools import cycle
from functional import seq

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


class Caesar:
    @classmethod
    def encode(cls, _text: str, offset: int) -> str:
        return seq(iter(_text))\
            .map(lambda c: chr((ord(c)-97+offset) % 26+97))\
            .make_string('')

    @classmethod
    def decode(cls, _text: str, offset: int) -> str:
        return seq(iter(_text))\
            .map(lambda c: chr((ord(c)-97-offset) % 26+97))\
            .make_string('')

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


class Playfair:
    alphabet = seq(list('abcdefghiklmnopqrstuvwxyz'))

    @classmethod
    def encode(cls, _text: str, _key: str, nullchar: str = 'q') -> str:
        key = seq(list(_key.lower()))
        text = seq(list(_text.lower().replace('j', 'i')))\
            .sliding(2)\
            .smap(lambda x, y: [x, y] if x != y else [x, nullchar, y])\
            .fold_left([_text[0]], lambda cur, next: cur + next[1:] if next else []) + [nullchar]
        table = ''.join(key.distinct().filter(lambda x: x != 'j') +
                        cls.alphabet.filter(lambda x: x not in _key))

        def opposite(a, b):
            pos = seq(a, b)\
                .map(lambda x: table.find(x))\
                .map(lambda x: (x//5, x % 5))
            if pos[0][0] == pos[1][0]:
                return pos.map(lambda x: table[(x[0]*5 + (x[1]+1) % 5)])
            if pos[0][1] == pos[1][1]:
                return pos.map(lambda x: table[(x[0]+1) % 5*5 + x[1]])
            return (
                table[pos[0][0]*5 + pos[1][1]],
                table[pos[1][0]*5 + pos[0][1]])

        return text\
            .grouped(2)\
            .filter(lambda x: len(x) == 2)\
            .map(lambda x: opposite(x[0], x[1]))\
            .flatten()\
            .make_string('')

    @classmethod
    def decode(cls, _text: str, _key: str) -> str:
        key = seq(list(_key.lower()))
        table = ''.join(key.distinct().filter(lambda x: x != 'j') +
                        cls.alphabet.filter(lambda x: x not in _key))
        text = seq(list(_text.lower())).grouped(2)

        def opposite(a, b):
            pos = seq(a, b)\
                .map(lambda x: table.find(x))\
                .map(lambda x: (x//5, x % 5))
            if pos[0][0] == pos[1][0]:
                return pos.map(lambda x: table[(x[0]*5 + (x[1]-1) % 5)])
            if pos[0][1] == pos[1][1]:
                return pos.map(lambda x: table[(x[0]-1) % 5*5 + x[1]])
            return (
                table[pos[0][0]*5 + pos[1][1]],
                table[pos[1][0]*5 + pos[0][1]])
        return text.smap(opposite).flatten().make_string('')


class Permutation:
    @classmethod
    def encode(cls, _text: str, _rule: List[int], nullchar: str = 'x') -> str:
        text = seq(list(_text + nullchar*(len(_rule) - len(_text) % len(_rule))))
        rule = seq(_rule)\
            .zip_with_index()\
            .sorted(lambda x: x[0])\
            .map(lambda x: x[1])\
            .list()
        return text\
            .grouped(len(rule))\
            .map(lambda x: [x[i] for i in rule])\
            .flatten()\
            .make_string('')

    @classmethod
    def decode(cls, _text: str, _rule: List[int]) -> str:
        '''
        rule = seq(_rule)\
            .zip_with_index()\
            .sorted(lambda x: x[1])\
            .map(lambda x: x[0])\
            .list()
            '''
        return seq(list(_text))\
            .grouped(len(_rule))\
            .map(lambda x: [x[i] for i in _rule])\
            .flatten()\
            .make_string('')


class ColumnPermutation:
    @classmethod
    def encode(cls, _text: str, _key: str, nullchar: str = 'x') -> str:
        width = len(_key)
        m = len(_text) % width
        if m != 0:
            _text += nullchar*(width-m)

        key = seq(list(_key))
        text = seq(list(_text.lower())).grouped(width)
        return key\
            .zip_with_index()\
            .sorted(lambda x: x[0])\
            .zip_with_index()\
            .sorted(lambda x: x[0][1])\
            .map(lambda x: x[1])\
            .map(lambda x: text.map(lambda y: y[x]))\
            .flatten()\
            .make_string('')
        '''
        key                             # t         e         e         m
            .zip_with_index()           # (t,0)     (e,1)     (e,2)     (m,3)
            .sorted(lambda x: x[0])     # (e,1)     (e,2)     (m,3)     (t,0)
            .zip_with_index()           # ((e,1),0) ((e,2),1) ((m,3),2) ((t,0),3)
            .sorted(lambda x: x[0][1])  # ((t,0),3) ((e,1),0) ((e,2),1) ((m,3),2)
            .map(lambda x: x[1])        # 3         0          1        2
        '''
    @classmethod
    def decode(cls, _text: str, _key: str) -> str:
        width = len(_key)
        height = len(_text)//width
        text = seq(list(_text.lower())).grouped(height).list()
        plain = seq(list(_key))\
            .zip_with_index()\
            .sorted(lambda x: x[0])\
            .map(lambda x: x[1])\
            .map(lambda x: text[x])\
            .list()
        ret = ''
        for i in range(height):
            for j in range(width):
                ret += plain[j][i]
        return ret

    @classmethod
    def double_encode(cls, _text: str, _key1: str, _key2: str, nullchar: str = 'x') -> str:
        return cls.encode(
            cls.encode(_text, _key1, nullchar),
            _key2
        )

    @classmethod
    def double_decode(cls, _text: str, _key1: str, _key2: str) -> str:
        return cls.decode(
            cls.decode(_text, _key2),
            _key1
        )


if __name__ == '__main__':
    assert Caesar.encode('abcdef', 28) == 'cdefgh'
    assert Caesar.decode('cdefgh', 28) == 'abcdef'
    assert Keyword.encode('abcdef', 'cfg') == 'cfgabd'
    assert Keyword.decode('cfgabd', 'cfg') == 'abcdef'
    assert Affine.encode('abcdef', 7, 12) == 'mtahov'
    assert Affine.decode('mtahov', 7, 12) == 'abcdef'
    assert Multiliteral.encode('abcdef', 'btrfs') == 'bbbtbrbfbstb'
    assert Multiliteral.decode('bbbtbrbfbstb', 'btrfs') == 'abcdef'
    assert Vigenere.encode('abcdef', 'amr') == 'antdqw'
    assert Vigenere.decode('antdqw', 'amr') == 'abcdef'
    assert AutokeyCipher.encode('ihopethisworks', 'alice') == 'iswribzejepqob'
    assert AutokeyCipher.decode('iswribzejepqob', 'alice') == 'ihopethisworks'
    assert AutokeyPlain.encode('ihopethisworks', 'alice') == 'iswribowhahysk'
    assert AutokeyPlain.decode('iswribowhahysk', 'alice') == 'ihopethisworks'
    assert Playfair.encode('nexttimejaytrysomethingdifferent', 'telegram') == \
        'hrvlolhblhcvetgypaleikkrbniohttlfr'
    assert Playfair.decode('hrvlolhblhcvetgypaleikkrbniohttlfr', 'telegram') == \
        'nextqtimeiaytrysomethingdifqferent'
    assert Permutation.encode(
        'codesandciphersarefun', [1, 3, 0, 2]) == 'dceonsdapchisearfruexnxx'
    assert Permutation.decode(
        'dceonsdapchisearfruexnxx', [1, 3, 0, 2]) == 'codesandciphersarefunxxx'
    assert ColumnPermutation.encode(
        'encryptionalgorithms', 'teem') == 'riliseyogtnpnohctarm'
    assert ColumnPermutation.decode(
        'riliseyogtnpnohctarm', 'teem') == 'encryptionalgorithms'
    assert ColumnPermutation.double_encode(
        'usingaciphertwicemayimprovethestrenthofthecipheroritmaynot',
        'what',
        'next'
    ) == 'irtnhvetthpianinyttamoapohoisectrsmergihmeecxrtixwehuerocpfy'
    assert ColumnPermutation.double_decode(
        'irtnhvetthpianinyttamoapohoisectrsmergihmeecxrtixwehuerocpfy',
        'what',
        'next'
    ) == 'usingaciphertwicemayimprovethestrenthofthecipheroritmaynotxx'
