#!/usr/bin/python3
from ran import randoms


class aot(object):
    def w(self, key1, key2, key3, arr):
        return (arr[key1] + arr[key2] + arr[key3])

    def aots(self, start, end, arr):
        matrix = [[0 for i in range(len(arr) + 1)]
                  for j in range(len(arr) + 1)]

        for i in range(start, end + 1):
            m = start
            n = i
            while m <= start + end - i and n <= end:
                if abs(m - n) <= 1:
                    matrix[m][n] = 0
                else:
                    matrix[m][n] = \
                        min([matrix[m][k]+matrix[k][n]+self.w(m, k, n, arr) for k in range(m+1, n)])
                m += 1
                n += 1
        return matrix[start][end]


if __name__ == "__main__":
    test = aot()
    a = test.aots(1, 10, randoms.list_int(11))
    print(a)
