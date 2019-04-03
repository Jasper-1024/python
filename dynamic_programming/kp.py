#!/usr/bin/python3
from ran import randoms


class kp(object):
    def kp_dp(self, weight, value, wlimted):
        lens = len(weight)
        matrix = [[0 for i in range(wlimted + 1)] for j in range(lens + 1)]

        for i in range(1, wlimted + 1):
            if i >= weight[1]:
                matrix[1][i] = value[1]
            else:
                matrix[1][i] = 0

        for m in range(2, lens + 1):
            for n in range(1, wlimted + 1):
                if n >= weight[m-1]:
                    matrix[m][n] = max(
                        matrix[m - 1][n],
                        matrix[m - 1][n - weight[m - 1]] + value[m - 1])
                else:
                    matrix[m][n] = matrix[m - 1][n]

        return matrix[lens][wlimted]


if __name__ == "__main__":
    test = kp()
    weight = randoms.list_int(11, 10)
    value = randoms.list_int(11, 10)
    a = test.kp_dp(weight, value, 50)
    print(a)