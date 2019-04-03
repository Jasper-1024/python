#!/usr/bin/python3
from ran import randoms


class bst(object):
    # p[0]为无效位
    def list_pq(self, size=10):
        tmp = randoms.list_int(size)
        tmq = randoms.list_int(size + 1)
        sums = sum(tmp) + sum(tmq)
        p = [x / sums for x in tmp]
        p.insert(0, 0)
        q = [x / sums for x in tmq]
        return [p, q]

    def w(self, k, i, j, p, q):
        return sum(p[i:j + 1]) + sum(q[i - 1:j + 1]) - q[k]

    def qbst(self, p, q):
        size = len(q)  # 0~n n+1个
        matrix = [[0 for i in range(size)] for j in range(size + 1)]

        for i in range(0, size):  # 填充第0斜线
            matrix[i + 1][i] = q[i]
        for i in range(1, size):  # 填充1~n斜线
            m = 1
            n = i
            while m < size and n < size:
                matrix[m][n] = min([
                    matrix[m][k - 1] + matrix[k + 1][n] + self.w(
                        k, m, n, p, q) for k in range(m, n + 1)
                ])
                m += 1
                n += 1
        return matrix[1][size - 1]


if __name__ == "__main__":
    test = bst()
    arr = test.list_pq()
    p = arr[0]
    q = arr[1]
    tmp = test.qbst(p, q)
    print(tmp)
