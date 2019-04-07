#!/usr/bin/python3

from ST import ST, HTNode, randoms


class lpht(ST):
    def __init__(self, tablesize=1, hash=hash):
        # hash表长度
        self.__tablesize = tablesize
        # 一个list
        self.__table = [None for i in range(self.__tablesize)]
        # 散列函数
        self.__hash = hash
        # 键值对数量
        self.__size = 0

    # 查找
    def search(self, key):
        return self.get(key)

    # 插入
    def insert(self, key, value):
        self.put(key, value)

    # 删除
    def delete(self, key):
        self.delete_node(key)

    def get(self, key):
        index = self.hash(key)
        # 探测直到遇到None
        while self.__table[index]:
            if self.__table[index].key == key:
                return self.__table[index].value
            index = (index + 1) % self.__tablesize
        return None

    def put(self, key, value):
        # 动态调整哈希表长度
        if self.__size > 0 and self.__size >= self.__tablesize // 2:
            self.resize(self.__tablesize * 2)

        index = self.hash(key)
        # 查找到下一个为空节点
        while self.__table[index]:
            # 已插入key
            if self.__table[index].key == key:
                self.__table[index].value = value
                return
            index = (index + 1) % self.__tablesize
        self.__table[index] = HTNode(key, value)
        self.__size += 1

    def delete_node(self, key):
        index = self.hash(key)
        # 探测直到遇到None/查找到待删除节点
        while self.__table[index]:
            if self.__table[index].key == key:
                break
            index = (index + 1) % self.__tablesize
        # 查找到待删除节点
        if self.__table[index]:
            # 删除
            self.__table[index] = None
            self.__size -= 1
            index = (index + 1) % self.__tablesize
            # 重新插入簇内剩余节点
            while self.__table[index]:
                key_b, value_b = self.__table[index].key, self.__table[
                    index].value
                self.__table[index] = None
                self.insert(key_b, value_b)
                index = (index + 1) % self.__tablesize

        if self.__size > 0 and self.__size <= self.__tablesize * 8:
            self.resize(self.__tablesize // 2)

    # 动态调整哈希表大小
    def resize(self, tablesize=5):
        if tablesize < 1:
            return
        self.__tablesize = tablesize
        tmpTable = self.__table
        # 新建表
        self.__table = [None for i in range(self.__tablesize)]
        self.__size = 0
        # 遍历旧表
        for i in tmpTable:
            # 不为空,放入新表,删除引用
            if i:
                self.put(i.key, i.value)
                del i

    # 散列函数
    def hash(self, key):
        return self.__hash(key) % self.__tablesize


if __name__ == "__main__":
    test = lpht()
    # d = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
    d = randoms.dict_int(n=300, wk=1000)
    keys = [key for key in d]
    for k, v in d.items():
        test.insert(k, v)
    for k, v in d.items():
        if test.search(k) != v:
            print('search faild')
    for k, v in d.items():
        test.delete(k)
        # if test.search(k) != v:
        #     print('search faild')
