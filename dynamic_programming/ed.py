#!/usr/bin/python3


class ed(object):
    def editdistance(self, stra, strb):
        matrix = [[0 for i in range(len(strb) + 1)]
                  for j in range(len(stra) + 1)]
        matrix[0][0] = 0
        for m in range(1, len(stra) + 1):
            matrix[m][0] = m
        for n in range(1, len(strb) + 1):
            matrix[0][n] = n
        for m in range(1, len(stra) + 1):
            for n in range(1, len(strb) + 1):
                matrix[m][n] = min(
                    matrix[m - 1][n] + 1, matrix[m][n - 1] + 1,
                    matrix[m - 1][n - 1] +
                    (0 if stra[m - 1] == strb[n - 1] else 1))

        return matrix[len(stra)][len(strb)]


if __name__ == "__main__":
    test = ed()
    tmp = test.editdistance('abcde', 'abcde')
    print(tmp)
