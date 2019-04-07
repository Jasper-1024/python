#!/usr/bin/python3
import random
import string


class randoms(object):
    @classmethod
    def r_int(self, w=100):
        return random.randint(0, w)

    @classmethod
    def r_str(self, k2=1):
        return ''.join(random.choices(string.ascii_lowercase, k=k2))

    @classmethod
    def list_int(self, n=50, w=100):
        return [randoms.r_int(w) for i in range(n)]

    @classmethod
    def matrix(self, size=10, limt=10):
        matrix = [[randoms.r_int(limt) for i in range(size)]
                  for j in range(size)]
        return matrix

    @classmethod
    def dict_int(self, n=50, key='int', wk=10000, value='int', wv=100):
        if key == 'int':
            keys = [randoms.r_int(wk) for i in range(n)]
        elif key == 'str':
            keys = [randoms.r_str(wk) for i in range(n)]
        else:
            raise ValueError('key must be an int!')
        if value == 'int':
            values = [randoms.r_int(wv) for i in range(n)]
        elif value == 'str':
            values = [randoms.r_str(wv) for i in range(n)]
        else:
            raise ValueError('value must be an int!')
        return dict(zip(keys, values))


if __name__ == "__main__":
    a = randoms.dict_int(n=10)
    print(a)
