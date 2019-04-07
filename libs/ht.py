#!/usr/bin/python3


class HTNode(object):
    def __init__(self, key=0, value=0, prior=None, next=None):
        self.key = key
        self.value = value
        self.prior = prior
        self.next = next

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        if not (isinstance(key, int) or isinstance(key, str)):
            raise ValueError('key must be int or str!')
        self.__key = key

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, values):
        if not (isinstance(values, int) or isinstance(values, str)):
            raise ValueError('value must be int or str!')
        self.__value = values

    @property
    def prior(self):
        return self.__prior

    @prior.setter
    def prior(self, prior):
        if not (isinstance(prior, HTNode) or prior is None):
            raise ValueError('prior must be HTNode!')
        self.__prior = prior

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if not (isinstance(next, HTNode) or next is None):
            raise ValueError('next must be HTNode!')
        self.__next = next
