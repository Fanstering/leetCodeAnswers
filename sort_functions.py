import random


def getrandomlist(n):
    '''返回一个长度为n的整数列表，数据范围[0,1000) '''
    tlist = []
    for i in range(n):
        tlist.append(random.randrange(1000))
    return tlist


def bubble_sort(list):  # O(n^2)
    n = len(list)
    if n <= 1:
        return list
    for i in range(n):  # 外循环从第二个数开始到最后一个数
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                # 实际上是将一个元组赋值给两个元素，所以不需要额外的交换变量
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def select_sort(list):  # O(n^2)
    n = len(list)
    if n <= 1:
        return list
    for i in range(n):  # 外循环从第二个数开始到最后一个数
        mix_index = i
        for j in range(i + 1, n):
            if list[j] < list[mix_index]:
                mix_index = j
        list[i], list[mix_index] = list[mix_index], list[i]
    return list


def insert_sort(list):  # O(n^2)
    n = len(list)
    if n <= 1:
        return list
    for i in range(1, n):  # 外循环从第二个数开始到最后一个数 默认第一个数已排序
        target = list[i]
        for j in range(i):  # 内循环遍历已排序的序列，将第i个数插进去
            if target < list[j]:  # i号位小于j号位时 将i号位插入j号位
                list[j + 1:i + 1] = list[j:i]  # 往后挪 腾出j号位置
                list[j] = target
                break  # 插入完成，即刻退出内循环
    return list


def merge_sort(list):  # 复杂度O(nlogn) 分治法 递归
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left, right = list[0:middle], list[middle:]
    return (merge_half(merge_sort(left), merge_sort(right)))


def merge_half(left, right):
    middle_list = []
    while left and right:
        if left[0] >= right[0]:
            middle_list.append(right.pop(0))
        else:
            middle_list.append(left.pop(0))
    while left:
        middle_list.append(left.pop(0))
    while right:
        middle_list.append(right.pop(0))
    return middle_list


def quick_sort_python(arr):  # python专有的实现方法，非常简洁 但莫得灵魂
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 选择基准点（中间点） 一般取最后一个，即arr[len(arr)-1]
    left = [x for x in arr if x < pivot]  # 比基准点小的元素放在左边
    middle = [x for x in arr if x == pivot]  # 等于基准点的元素放在中间
    right = [x for x in arr if x > pivot]  # 比基准点大的元素放在右边

    return quick_sort_python(left) + middle + quick_sort_python(right)


def quick_sort(list, low, high):  # nlogn
    if low >= high:
        return
    pivot_index = partition(list, low, high)
    quick_sort(list, low, pivot_index - 1)
    quick_sort(list, pivot_index + 1, high)


def partition(list, low, high):
    pivot = list[low]  # 初始基准点为0
    left = low
    right = high
    index = low
    while right > left:
        while right > left:
            if list[right] < pivot:
                list[left] = list[right]
                index = right
                left += 1
                break
            right -= 1
        while right > left:
            if list[left] > pivot:
                list[right] = list[left]
                index = left
                right -= 1
                break
            left += 1
    list[index] = pivot
    return index


# 线性时间复杂度的排序算法：计数排序，用于对整数排序，用空间换时间

# 计数排序（Counting Sort）是一种非比较排序算法，适用于特定范围内的整数排序。
# 它的基本思想是统计数组中每个元素的出现次数，然后根据这些统计信息将元素放置到正确的位置上。
# 计数排序是一种稳定的线性时间排序算法，时间复杂度为 O(n + k)，其中 n 是待排序数组的长度，k 是待排序数组中元素的取值范围（即最大值与最小值的差加 1）。
# 计数排序的时间复杂度分析如下：
# **统计元素出现次数：**首先遍历待排序数组，统计每个元素出现的次数，需要 O(n) 的时间复杂度。
# **构建排序后的数组：**然后根据统计信息重新构建排序后的数组，需要遍历统计数组，时间复杂度为 O(k)。
# **输出排序结果：**最后将排序后的数组输出，时间复杂度为 O(n)。
# 因此，总的时间复杂度为 O(n + k)。需要注意的是，当 k 较小且与 n 无关时，计数排序的时间复杂度可以近似为 O(n)。

def counting_sort(arr):
    # 找出数组中的最大值和最小值
    max_val = max(arr)
    min_val = min(arr)

    # 统计每个元素的出现次数
    count = [0] * (max_val - min_val + 1)
    for num in arr:
        count[num - min_val] += 1

    # 根据统计信息重新构建排序后的数组
    sorted_arr = []
    for i in range(min_val, max_val + 1):  # 遍历count数组
        sorted_arr.extend([i] * count[i - min_val])

    return sorted_arr


def bucket_sort(arr, bucket_size=10):
    # 创建桶并初始化为空列表
    n = len(arr)
    max_val = max(arr)
    min_val = min(arr)
    # bucket_size是桶的数量，可以根据数据范围和数量进行调整
    bucket_range = (max_val - min_val) / bucket_size  # 计算桶的范围

    buckets = [[] for _ in range(bucket_size)]

    # 将数据分配到各个桶中
    for num in arr:
        index = int((num - min_val) // bucket_range)
        if index != bucket_size:
            buckets[index].append(num)
        else:  # 如果是最大值 放入最后一个桶中
            buckets[bucket_size - 1].append(num)

    # 对每个桶中的数据进行排序
    for bucket in buckets:
        bucket.sort()

    # 合并桶中的数据
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


def heapify(arr, n, i):
    """
        arr:    序列
        n:      长度
        i:      根结点
    """
    largest = i  # 初始化根结点
    l = 2 * i + 1  # 左子树
    r = 2 * i + 2  # 右子树
    # 如果左子节点存在且大于根节点，则更新最大值索引
    if l < n and arr[l] > arr[largest]:
        largest = l

    # 如果右子节点存在且大于根节点，则更新最大值索引
    if r < n and arr[r] > arr[largest]:
        largest = r

    # 如果最大值索引不等于根节点索引，则交换根节点和最大值节点，并递归调用堆化函数
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # 构建最大堆 假设数组的长度为n，则最后一个非叶子节点的索引为(n // 2 - 1)，
    # 因为它是最后一个节点的父节点。我们从最后一个非叶子节点开始向前遍历到根节点，
    # 依次对每个节点进行堆化操作，从而构建最大堆。
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 依次取出堆顶元素（最大值）并调整堆结构
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换堆顶元素和当前末尾元素
        heapify(arr, i, 0)  # 调整堆
    return arr


if __name__ == "__main__":
    # tlist = getrandomlist(10)
    tlist = [177, 835, 529, 727, 412, 20, 1, 11, 974, 240]
    print(tlist)
    result = [1, 11, 20, 177, 240, 412, 529, 727, 835, 974]
    print("groundtruth:\n", result)
    # print(bubble_sort(tlist))
    # print(select_sort(tlist))
    # print(insert_sort(tlist))
    # print(tlist)
    # print(merge_sort(tlist))
    # print(quick_sort_python(tlist))
    # quick_sort(tlist, 0, len(tlist) - 1)
    # print(tlist)
    # print(counting_sort(tlist))
    # print(bucket_sort(tlist))
    print(heap_sort(tlist))
