def binary_search(arr, target):  # 二分查找，时间复杂度O(logn)
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # 如果目标值等于中间值，则返回中间值的索引
        if arr[mid] == target:
            return mid
        # 如果目标值小于中间值，则在左半边继续查找
        elif arr[mid] > target:
            right = mid - 1
        # 如果目标值大于中间值，则在右半边继续查找
        else:
            left = mid + 1

    # 如果未找到目标值，则返回 -1
    return -1


def interpolation_search(arr, key):  # 时间复杂度O(loglogn)
    """
    步骤：1. 计算大概的查询元素位置
    计算公式为： 先计算下标之差/首尾元素之差，获得数组中下标与数值的对应比例，然后乘以待查询元素与列表首个元素的差值，
    得到待查询元素在列表中的大概比例，再加上low得到具体的下标
    2. 查看待查位置是否有待查元素，如果有就返回，如果小于待查元素，就将Low设置为当前位置，从后面的列表中查，反之从前面查

    :param arr: 用来查询的有序数组
    :param key: 待查询元素
    :return:    查询到的下标，未查询到则返回-1
    """

    low = 0  # 搜索位置的首端
    high = len(arr) - 1  # 搜索位置的末端
    # 判定条件，low <= high 是循环退出条件 arr[low] <= key <= arr[high]则确保arr如果不是有序列表可能引起的除0溢出问题

    while (low <= high and arr[low] <= key <= arr[high]):
        mid = low + int((key - arr[low]) * (high - low) / (arr[high] - arr[low]))
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# 顺序查找的数列可以是无序的，而二分查找和插值查找要求数组有序
# 介于两种方法之间的 分块查找，只要求块间有序，块内可以无序

def block_search(arr, block_size: int, key) -> int:
    """

    1. 建立一个块索引数组，存储了每个块的一个代表性的值（一般是最大值或者最小值）
    2. 先查询索引数组，确定待查询元素会出现在哪个块中
    3. 再查询块数组，准确查询
    :param arr:        查询数组
    :param block_size: 块大小
    :param key:        待查询元素
    :return:           查询位置，没有返回-1
    """
    n = len(arr)
    num_blocks = n // block_size + (1 if n % block_size != 0 else 0)

    # 构建索引表
    index = []
    for i in range(num_blocks):
        start = i * block_size
        end = min((i + 1) * block_size, n)  # min确保不越界
        index.append((start, arr[start]))  # 索引表有两列，第一列是块号，第二列是块的代表元素

    # 在索引表中查找对应块
    block_index = -1
    for i in range(num_blocks):
        if index[i][1] <= key:  # 如果当前索引值小于等于目标值 记录索引号
            block_index = i  # 继续循环保证落入正确的块中

    # 在对应块内进行线性查找  当然如果数据量大且有序，也可以用二分或者差值查询
    if block_index != -1:
        start, _ = index[block_index]
        end = min((block_index + 1) * block_size, n)
        for i in range(start, end):
            if arr[i] == key:
                return i

    return -1


# 测试
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 13
result = binary_search(arr, target)
result = interpolation_search(arr, target)
block_size = 10
result = block_search(arr, block_size, target)

if result != -1:
    print(f"目标值 {target} 在数组中的索引为 {result}")
else:
    print(f"目标值 {target} 未在数组中找到")
