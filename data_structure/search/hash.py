#!/usr/bin/python3

from ST import ST, HTNode, randoms


class sc(ST):
    def __init__(self, tablesize=1, hash=hash):
        # hash表长度
        self.__tablesize = tablesize
        self.__table = [[] for i in range(self.__tablesize)]
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
        # 对应链表为空
        if len(self.__table[index]) == 0:
            return None
        else:
            for item in self.__table[index]:
                if item.key == key:
                    return item.value
        return None

    def put(self, key, value):
        index = self.hash(key)
        # 链表为空
        if len(self.__table[index]) == 0:
            self.__table[index].insert(0, HTNode(key, value))
            self.__size += 1
        else:
            for item in self.__table[index]:
                # 在链表内
                if item.key == key:
                    item.value = value
                    return
            # 未在链表,表头插入
            self.__table[index].insert(0, HTNode(key, value))
            self.__size += 1
        # 动态调整哈希表长度.
        if self.__size > 0 and self.__size >= self.__tablesize * 5:
            self.resize(self.__tablesize * 2)

    def delete_node(self, key):
        index = self.hash(key)
        if len(self.__table[index]) == 0:
            return
        else:
            for i, item in enumerate(self.__table[index]):
                if item.key == key:
                    self.__table[index].pop(i)
                    self.__size -= 1
        if self.__size > 0 and self.__size <= self.__tablesize * 2:
            self.resize(self.__tablesize // 2)

    # 动态调整哈希表大小
    def resize(self, tablesize=5):
        if tablesize < 1:
            return
        self.__tablesize = tablesize
        tmpTable = self.__table
        # 新建表
        self.__table = [[] for i in range(self.__tablesize)]
        self.__size = 0
        # 遍历旧表
        for i in tmpTable:
            if len(i) != 0:
                for j in i:
                    # 放入新表,删除引用
                    self.put(j.key, j.value)
                    del j
            del i

    # 散列函数
    def hash(self, key):
        return self.__hash(key) % self.__tablesize


if __name__ == "__main__":
    test = sc()
    d = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
    d = randoms.dict_int(n=300, wk=1000)
    keys = [key for key in d]
    for k, v in d.items():
        test.insert(k, v)
    for k, v in d.items():
        test.delete(k)
