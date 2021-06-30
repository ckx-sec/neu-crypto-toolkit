from typing import List
from functional import seq


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
