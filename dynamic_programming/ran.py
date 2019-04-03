#!/usr/bin/python3
import random
import secrets
import timeit


class randoms(object):
    @classmethod
    def list_int(self, n=50, w=100):
        return [random.randint(0, w) for i in range(n)]

    @classmethod
    def matrix(self, size=10, limt=10):
        matrix = [[random.randint(0, limt) for i in range(size)]
                  for j in range(size)]
        return matrix

    @classmethod
    def list_str(self, lens=20, capital=True):
        return secrets.token_urlsafe(lens)

    @classmethod
    def time(self, method, setus):
        if callable(method):
            if isinstance(setus, str):
                print(timeit.timeit(method, number=10, setup=setus))
            else:
                print('setus is not str')
        else:
            print("%s is not a method" % method)


# if __name__ == "__main__":
#    arr = randoms.list_int()
#    print(arr)
#    randoms.time(randoms.list_int, 'from ran import randoms')
