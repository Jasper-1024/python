#!/usr/bin/python3
from ran import randoms


class floyd(object):
    def floyd_N3(self, G):
        size = len(G[0])
        matrix3 = [[[0 for i in range(size)] for j in range(size)]
                   for k in range(size)]
        matrix3[0] = G[:]  # 初始矩阵

        for k in range(1, size):
            for i in range(size):
                for j in range(size):
                    matrix3[k][i][j] = min(
                        matrix3[k - 1][i][j],
                        matrix3[k - 1][i][k] + matrix3[k - 1][k][j])
        return matrix3[size - 1]

    def floyd_N2(self, G):
        size = len(G[0])
        matrix1 = [[0 for i in range(size)] for j in range(size)]
        matrix2 = [[0 for i in range(size)] for j in range(size)]

        matrix1 = G[:]  # 初始矩阵

        for k in range(1, size):
            for i in range(size):
                for j in range(size):
                    matrix2[i][j] = min(matrix1[i][j],
                                        matrix1[i][k] + matrix1[k][j])
            matrix1 = matrix2[:]
        return matrix2

    def floyd_N22(self, G):
        size = len(G[0])
        matrix = G[:]  # 初始矩阵
        for k in range(1, size):
            for i in range(size):
                for j in range(size):
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
        return matrix


if __name__ == "__main__":
    tmp = randoms.matrix()
    #    print(tmp)
    test = floyd()
    tm = test.floyd_N3(tmp)
    tn = test.floyd_N2(tmp)
    ts = test.floyd_N22(tmp)
    print(tm)
    print(tn)
    print(ts)
