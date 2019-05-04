#!/usr/bin/python3


class test(object):
    def base(self):
        return 'b'


def gt(t: test = test(), a: int = 1) -> str:
    return 'hello'


if __name__ == "__main__":
    t = test()
    gt(t, "2")
    gt()
