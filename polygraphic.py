from functional import seq


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


if __name__ == '__main__':
    assert Playfair.encode('nexttimejaytrysomethingdifferent', 'telegram') == \
        'hrvlolhblhcvetgypaleikkrbniohttlfr'
    assert Playfair.decode('hrvlolhblhcvetgypaleikkrbniohttlfr', 'telegram') == \
        'nextqtimeiaytrysomethingdifqferent'
