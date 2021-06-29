from functional import seq


class Caesar():
    def __init__(self, text: str) -> None:
        self.text = text

    def encode(self, offset: int) -> str:
        return seq(list(self.text))\
            .map(lambda c: chr((ord(c)-65+offset) % 26+65))\
            .make_string('')

    def decode(self, offset: int) -> str:
        return seq(list(self.text))\
            .map(lambda c: chr((ord(c)-65-offset) % 26+65))\
            .make_string('')


class Keyword():
    def __init__(self, text: str) -> None:
        self.text = text

    def encode(self, keyword: str):
        alphabet = seq(list('abcdefghijklmnopqrstuvwxyz'))
        table = alphabet.zip(
            keyword + alphabet.filter(lambda x: x not in keyword)
        ).dict()
        return seq(list(self.text)).map(lambda x: table[x]).make_string('')
