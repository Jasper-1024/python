#!/usr/bin/python3
from ran import randoms
import functools


class lis(object):
    @classmethod
    def lis_dp(self, arr):
        # dp = [0 for x in range(0, len(arr))]
        dp = [0] * len(arr)
        for i, valuei in enumerate(arr):
            for j, valuej in enumerate(arr[0:i]):
                if valuej <= valuei and dp[j] > dp[i]:
                    dp[i] = dp[j]
            dp[i] += 1
        return max(dp)

    @classmethod
    def lis_dp_binse(self, arr):
        tails = [0] * len(arr)
        size = 0
        for x in arr:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] <= x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size


if __name__ == "__main__":
    arr = randoms.list_int(500)
    n = functools.partial(lis.lis_dp, arr)
    s = functools.partial(lis.lis_dp_binse, arr)
    randoms.time(n, 'from lis import lis'),
    randoms.time(s, 'from lis import lis')
