# 代码题：给整数数组和target，找数组当中和为目标值的两个整数返回下标。

# 使用一个字典来存储遍历过的数字及其下标，
# 通过查找字典来判断是否存在与当前数字配对的数字，
# 从而实现寻找和为目标值的两个数的功能。
def two_sum(nums, target):
    num_dict = {}  # 用字典存储数字和对应的下标
    for i, num in enumerate(nums):
        complement = target - num  # 计算目标值与当前值的差值
        if complement in num_dict:  # 如果差值在字典中，则找到了符合条件的两个数
            return [num_dict[complement], i]
        num_dict[num] = i  # 否则将当前数字及其下标存入字典
    return None  # 如果未找到符合条件的两个数，则返回None


# 示例
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # 输出 [0, 1]，因为 nums[0] + nums[1] = 2 + 7 =

# 整体时间复杂度为O(n) 因为遍历计算一次当前值与目标值的差值就够了，查询这个差值是否在字典中只需要O(1)的时间复杂度，因为字典使用哈希表存储的
# 哈希表查询的平均时间复杂度为O(1)，最差情况才是O(n)

# 从这题得到启发：这种组合匹配target的情况，要用字典的哈希特性来节省时间复杂度