#!/usr/bin/python3

from sort_base import randoms
import sys
import random
import time
import functools


def exeTime(func):
    @functools.wraps(func)
    def newFunc(*args, **args2):
        start = time.time()
        func(*args, **args2)
        end = time.time()
        print('{%s} exec %f' % (func.__name__, end - start))
        return func(*args, **args2)

    return newFunc


class sort(object):
    # 选择排序
    @exeTime
    def selectionsort(self, arr):
        for i in range(len(arr)):
            minindex = i
            # 选择未排序序列最小值
            for j in range(i + 1, len(arr)):
                if arr[minindex] > arr[j]:
                    minindex = j
            if i == minindex:
                pass
            else:
                arr[i], arr[minindex] = arr[minindex], arr[i]
        return arr

    # 插入排序
    @exeTime
    def InsertSort(self, arr):
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i - 1
            # 由后向前扫描
            while j >= 0 and temp < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = temp
        return arr

    # 希尔排序
    @exeTime
    def ShellSort(self, arr):
        n = len(arr)
        # 初始步长
        gap = (n - 1) // 3
        while gap > 0:
            for i in range(gap, n):
                # 每个步长进行插入排序
                temp = arr[i]
                j = i
                # 插入排序
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            # 得到新的步长
            gap = (gap - 1) // 3
        return arr

    # 冒泡排序
    @exeTime
    def BubbleSort(self, arr):
        list_len = len(arr)
        for i in range(list_len - 1):
            for j in range(list_len - 1, i, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
        return arr

    # 归并排序
    @exeTime
    def MergeSort(self, arr):
        def merge(left, right):
            # 最大值小于最小值,跳过合并
            if left[0] >= right[-1]:
                result = right + left
            elif left[-1] <= right[0]:
                result = left + right
            else:
                # 正常合并过程
                result = []
                # 取元素直到某个序列为空
                while left and right:
                    if left[0] <= right[0]:
                        result.append(left.pop(0))
                    else:
                        result.append(right.pop(0))
                # 合并剩余不为空的序列
                if left:
                    result += left
                if right:
                    result += right
            return result

        def sort(arr):
            # 序列长度为1
            if len(arr) <= 1:
                return arr
            # 取中间值
            mid = len(arr) // 2
            # 递归调用
            left = sort(arr[:mid])
            right = sort(arr[mid:])
            # 归并
            return merge(left, right)

        sort(arr)

    # 快速排序
    @exeTime
    def QuickSort(self, arr):
        lens = len(arr) - 1

        def simplerandom(arr, start, end):
            return (start + end) // 2

        def partition(arr, start, end, i):
            # 交换切分元素到最后
            arr[i], arr[end] = arr[end], arr[i]
            i = start - 1
            for j in range(start, end):
                # 一次交换一个元素到确定位置
                if arr[j] < arr[end]:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            # 防止最坏情况发生
            arr[i + 1], arr[end] = arr[end], arr[i + 1]
            return i + 1

        def sort(arr, start, end):
            if start >= end:
                return
            # 选取切分元素
            i = simplerandom(arr, start, end)
            # 中间位置
            p = partition(arr, start, end, i)
            sort(arr, start, p - 1)
            sort(arr, p + 1, end)

        sort(arr, 0, lens)
        return arr

    # 快速排序
    @exeTime
    def QuickSort_random(self, arr):
        lens = len(arr) - 1

        # 随机抽样
        def simplerandom(arr, start, end):
            return random.randint(start, end)

        def partition(arr, start, end, i):
            # 交换切分元素到最后
            arr[i], arr[end] = arr[end], arr[i]
            i = start - 1
            for j in range(start, end):
                # 一次交换一个元素到确定位置
                if arr[j] < arr[end]:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            # 防止最坏情况发生
            arr[i + 1], arr[end] = arr[end], arr[i + 1]
            return i + 1

        def sort(arr, start, end):
            if start >= end:
                return
            # 选取切分元素
            i = simplerandom(arr, start, end)
            # 中间位置
            p = partition(arr, start, end, i)
            sort(arr, start, p - 1)
            sort(arr, p + 1, end)

        sort(arr, 0, lens)
        return arr

    # 快速排序
    @exeTime
    def QuickSort_three(self, arr):
        lens = len(arr) - 1

        # 三抽样
        def three(arr, start, end):
            mid = (start + end) // 2
            a = arr[start] < arr[mid]
            b = arr[mid] < arr[end]
            c = arr[start] < arr[end]
            if a and b:
                i = mid
            elif c and (not b):
                i = end
            elif c and (not a):
                i = start
            elif b and (not c):
                i = end
            elif a and (not c):
                i = start
            else:
                i = mid
            return i

        def partition(arr, start, end, i):
            # 交换切分元素到最后
            arr[i], arr[end] = arr[end], arr[i]
            i = start - 1
            for j in range(start, end):
                # 一次交换一个元素到确定位置
                if arr[j] < arr[end]:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            # 防止最坏情况发生
            arr[i + 1], arr[end] = arr[end], arr[i + 1]
            return i + 1

        def sort(arr, start, end):
            if start >= end:
                return
            # 选取切分元素
            i = three(arr, start, end)
            # 中间位置
            p = partition(arr, start, end, i)
            sort(arr, start, p - 1)
            sort(arr, p + 1, end)

        sort(arr, 0, lens)
        return arr

    # sink
    def sink(self, arr, i, heap_size):
        largest = i
        # 如果左子树较大
        if 2 * i <= heap_size and arr[2 * i] > arr[i]:
            largest = 2 * i
        # 如果右子树较大
        if 2 * i + 1 <= heap_size and arr[2 * i + 1] > arr[largest]:
            largest = 2 * i + 1
        # 发生交换,递归调用
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.sink(arr, largest, heap_size)

    # 堆排序
    @exeTime
    def HeapSort(self, arr):
        # 二叉堆的长度
        heap_size = len(arr)
        # 堆排序由索引1开始,插入一个元素.
        arr.insert(0, 0)
        # 构造最大堆
        for i in range(heap_size // 2, 0, -1):
            self.sink(arr, i, heap_size)
        # 堆排序
        while heap_size > 1:
            arr[1], arr[heap_size] = arr[heap_size], arr[1]
            heap_size -= 1
            self.sink(arr, 1, heap_size)
        # 删除插入元素
        arr.pop(0)
        return arr


class quicksort(object):
    # 快速排序a
    @exeTime
    def simple_a(self, arr):
        lens = len(arr) - 1
        self.sort(arr, 0, lens, self.choose_simple, self.partition_a)
        return arr

    # 快速排序a_inser
    @exeTime
    def simple_a_inser(self, arr):
        lens = len(arr) - 1
        self.sort_inser(arr, 0, lens, self.choose_simple, self.partition_a)
        return arr

    # 快速排序b
    @exeTime
    def simple_b(self, arr):
        lens = len(arr) - 1
        self.sort(arr, 0, lens, self.choose_simple, self.partition_b)
        return arr

    # 快速排序b
    @exeTime
    def simple_b_inser(self, arr):
        lens = len(arr) - 1
        self.sort_inser(arr, 0, lens, self.choose_simple, self.partition_b)
        return arr

    @exeTime
    def random_a(self, arr):
        lens = len(arr) - 1
        self.sort(arr, 0, lens, self.choose_random, self.partition_a)
        return arr

    # 快速排序b
    @exeTime
    def random_b(self, arr):
        lens = len(arr) - 1
        self.sort(arr, 0, lens, self.choose_random, self.partition_b)
        return arr

    @exeTime
    def three_a(self, arr):
        lens = len(arr) - 1
        self.sort(arr, 0, lens, self.choose_three, self.partition_a)
        return arr

    @exeTime
    def three_a_inser(self, arr):
        lens = len(arr) - 1
        self.sort_inser(arr, 0, lens, self.choose_three, self.partition_a)
        return arr

    # 快速排序b
    @exeTime
    def three_b(self, arr):
        lens = len(arr) - 1
        self.sort(arr, 0, lens, self.choose_three, self.partition_b)
        return arr

    # 快速排序b
    @exeTime
    def three_b_inser(self, arr):
        lens = len(arr) - 1
        self.sort_inser(arr, 0, lens, self.choose_three, self.partition_b)
        return arr

    @exeTime
    def sort3_simple(self, arr):
        lens = len(arr) - 1
        self.sort3(arr, 0, lens, self.choose_simple, self.partition_3)
        return arr

    @exeTime
    def sort3_simple_inser(self, arr):
        lens = len(arr) - 1
        self.sort3_inser(arr, 0, lens, self.choose_simple, self.partition_3)
        return arr

    @exeTime
    def sort3_random(self, arr):
        lens = len(arr) - 1
        self.sort3(arr, 0, lens, self.choose_random, self.partition_3)
        return arr

    @exeTime
    def sort3_three(self, arr):
        lens = len(arr) - 1
        self.sort3(arr, 0, lens, self.choose_three, self.partition_3)
        return arr

    @exeTime
    def sort3_three_inser(self, arr):
        lens = len(arr) - 1
        self.sort3_inser(arr, 0, lens, self.choose_three, self.partition_3)
        return arr

    # 取固定值
    def choose_simple(self, arr, start, end):
        return (start + end) // 2

    # 随机抽样
    def choose_random(self, arr, start, end):
        return random.randint(start, end)

    # 三抽样
    def choose_three(self, arr, start, end):
        mid = (start + end) // 2
        a = arr[start] < arr[mid]
        b = arr[mid] < arr[end]
        c = arr[start] < arr[end]
        if a and b:
            i = mid
        elif c and (not b):
            i = end
        elif c and (not a):
            i = start
        elif b and (not c):
            i = end
        elif a and (not c):
            i = start
        else:
            i = mid
        return i

    # 切分普通
    def partition_a(self, arr, start, end, i):
        # 交换切分元素到最后
        arr[i], arr[end] = arr[end], arr[i]
        i = start - 1
        for j in range(start, end):
            # 一次交换一个元素到确定位置
            if arr[j] < arr[end]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        # 防止最坏情况发生
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        return i + 1

    # 切分
    def partition_b(self, arr, start, end, i):
        # 交换切分元素到最后
        arr[i], arr[end] = arr[end], arr[i]
        left, right, partition = start, end - 1, arr[end]
        while left < right:
            # 选取左边需要交换的元素
            while left < right and arr[left] < partition:
                left += 1
            # 选取右边需要交换的元素
            while left < right and arr[right] >= partition:
                right -= 1
            # 交换
            arr[left], arr[right] = arr[right], arr[left]
        # 如果右指针未动
        if arr[right] < arr[end]:
            right += 1
        else:
            arr[right], arr[end] = arr[end], arr[right]
        return right

    # 切分3
    def partition_3(self, arr, start, end, i):
        arr[i], arr[start] = arr[start], arr[i]
        left, right, i = start, end, start + 1
        # 切分元素
        partition = arr[start]
        while i <= right:
            cmp = arr[i] - partition
            # 小于切分元素
            if cmp < 0:
                arr[i], arr[left] = arr[left], arr[i]
                left, i = left + 1, i + 1
            # 大于切分元素
            elif cmp > 0:
                arr[i], arr[right] = arr[right], arr[i]
                right -= 1
            # 等于切分元素
            else:
                i += 1
        return (left, right)

    def sort(self, arr, start, end, choose, partition):
        if start >= end:
            return
        # 选取切分元素
        i = choose(arr, start, end)
        # 中间位置
        p = partition(arr, start, end, i)
        self.sort(arr, start, p - 1, choose, partition)
        self.sort(arr, p + 1, end, choose, partition)

    def sort_inser(self, arr, start, end, choose, partition):
        if (start + 5) >= end:
            self.InsertSort(arr, start, end)
            return
        # 选取切分元素
        i = choose(arr, start, end)
        # 中间位置
        p = partition(arr, start, end, i)
        self.sort_inser(arr, start, p - 1, choose, partition)
        self.sort_inser(arr, p + 1, end, choose, partition)

    # 3向切分
    def sort3(self, arr, start, end, choose, partition3):
        if start >= end:
            return
        # 选取切分元素
        i = choose(arr, start, end)
        # 中间位置
        p = partition3(arr, start, end, i)
        self.sort3(arr, start, p[0] - 1, choose, partition3)
        self.sort3(arr, p[1] + 1, end, choose, partition3)

    # 3向切分
    def sort3_inser(self, arr, start, end, choose, partition3):
        if (start + 5) >= end:
            self.InsertSort(arr, start, end)
            return
        # 选取切分元素
        i = choose(arr, start, end)
        # 中间位置
        p = partition3(arr, start, end, i)
        self.sort3_inser(arr, start, p[0] - 1, choose, partition3)
        self.sort3_inser(arr, p[1] + 1, end, choose, partition3)

    def InsertSort(self, arr, start, end):
        for i in range(start, end + 1):
            temp = arr[i]
            j = i - 1
            # 由后向前扫描
            while j >= 0 and temp < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = temp
        return arr


if __name__ == "__main__":
    sys.setrecursionlimit(100000)  # 例如这里设置为十万
    arr = randoms.list_int(n=50000, w=100)
    #   test = sort()
    #    select = test.selectionsort(arr.copy())
    #    print('\n')
    #    ins = test.InsertSort(arr.copy())
    #    print('\n')
    #   shell = test.ShellSort(arr.copy())ulimit -a
    #    print('\n')
    #    bu = test.BubbleSort(arr.copy())
    #    print('\n')
    #   merge = test.MergeSort(arr.copy())
    #   print('\n')
    #   qucik = test.QuickSort(arr.copy())
    #   print('\n')
    #   qucik = test.QuickSort_random(arr.copy())
    #   print('\n')
    #    qucik = test.QuickSort_three(arr.copy())
    #    print('\n')
    #   heap = test.HeapSort(arr.copy())
    #   print('\n')
    #   test = sort()
    #   quci = test.QuickSort(arr.copy())

    quicksort = quicksort()
    quicksort.simple_a(arr.copy())
    quicksort.three_a_inser(arr.copy())
    quicksort.simple_b(arr.copy())
    quicksort.simple_b_inser(arr.copy())
    quicksort.random_a(arr.copy())
    quicksort.random_b(arr.copy())
    quicksort.three_a(arr.copy())
    quicksort.three_a_inser(arr.copy())
    quicksort.three_b(arr.copy())
    quicksort.three_b_inser(arr.copy())
    quicksort.sort3_simple(arr.copy())
    quicksort.sort3_simple_inser(arr.copy())
    quicksort.sort3_random(arr.copy())
    quicksort.sort3_three(arr.copy())
    quicksort.sort3_three_inser(arr.copy())
