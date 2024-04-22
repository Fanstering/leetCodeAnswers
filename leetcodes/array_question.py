#数组相关问题
# 解题思路：双指针、对撞指针、滑动窗口

# 移动零（leetcode283）给定一个数组，将所有0移动到数组末尾，同时保持非零元素的相对顺序
# 必须在原数组上操作，不能拷贝额外的数组，尽量减少操作次数
# 方案1 如果可以拷贝额外的数组，那么可以遍历数组，遇到非零的就复制到新数组中，遍历结束后，在新数组后追加所有的0
def moveZeroes(nums) -> None:
    temp = []
    for i in range(len(nums)): # 启用新数组的情况
        if nums[i] != 0:
            temp.append(nums[i])
    for i in range(len(temp)): # 修改原数组
        nums[i] = temp[i]
    for i in range(len(temp), len(nums)): # 追加0
        nums[i] = 0
    print(nums)

# 双指针 i,j 从左向右遍历，j记录非零元素位置，i遇到非零元素时，赋值给J的位置，然后j向后移动
# 相当于两个人跑同一趟路，一个在前面捡，另一个在后面装 最后再用0补齐 比第一种方案更节省内存，因为是原地操作
def moveZeroes2(nums) -> None:
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    for i in range(j, len(nums)):
        nums[i] = 0

    print(nums)

# 对撞指针（交换情况） i先遍历，遇到非0元素就和j调换位置
def moveZeroes3(nums) -> None:
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1

    print(nums)
# ------------------------------------------------------
# 移除元素（leetcode27）
# 给定一个数组nums和一个值val，原地移除所有数值等于val的元素，并返回数组新长度
# 元素顺序可以改变

# 和前面的移动0显然是类似的思路，甚至如果把移动0理解为去除0，那就是一个题
# 双指针 i遇到非val值就赋值给j，然后i++,j++ 最后j指向的位置就是新长度 时间复杂度O(n),空间O(1)
def removeElement(nums, val) -> int:
    j = -1
    for i in range(len(nums)):
        if nums[i] != val:
            j += 1
            nums[j] = nums[i]

    return j + 1



# 删除有序数组的重复项（leetcode26）
# 给定升序排列的数组nums, 原地删除重复元素，返回删除后数组的新长度，相对顺序应一致，也就是要稳定有序。
# 原地操作，O（1）空间复杂度
# 其实和前面两题仍然类似，只是判断条件改了
# 依然是双指针，i遍历，如果和上个位置值不同，赋给j,然后i++,j++

def removeDuplicates(nums):
    if not nums:
        return 0

    n = len(nums)
    fast = slow = 1
    while fast < n:
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    print(nums)
    return slow


# 删除有序数组的重复项2（leetcode80）
#  给定升序排列的数组nums, 原地删除重复2次以上的元素，返回删除后数组的新长度，相对顺序应一致，也就是要稳定有序。
# 这次可以重复，但不能有三个及以上的重复 只需要将判定条件改成j-2和i的比较就行了
def removeDuplicates2(nums):
    n = len(nums)
    if n <= 2: # 小于3个数的话直接返回就行
        return n
    slow, fast = 2, 2
    while fast < n:
        if nums[slow - 2] != nums[fast]: # 判断当前数字是否和前两个相同
            nums[slow] = nums[fast]  # 相同的话，覆盖掉
            slow += 1
        fast += 1

    return slow
def sortColors(nums):
    n = len(nums)
    p0, p2 = 0, n - 1
    i = 0
    while i <= p2:
        while i <= p2 and nums[i] == 2:
            nums[i], nums[p2] = nums[p2], nums[i]
            p2 -= 1
        if nums[i] == 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            p0 += 1
        i += 1

def twoSum(numbers, target):
    low, high = 0, len(numbers) - 1
    while low < high:
        total = numbers[low] + numbers[high]
        if total == target:
            return [low + 1, high + 1]
        elif total < target:
            low += 1
        else:
            high -= 1

    return [-1, -1]

def removeElement2(nums, val) -> int:
    left = 0
    right = len(nums)
    while left < right:
        if nums[left] == val:
            nums[left] = nums[right - 1]
            right -= 1
        else:
            left += 1
    return left
def minSubArrayLen(target, nums):
    if not nums:
        return 0

    n = len(nums)
    ans = n + 1
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total >= target:
                ans = min(ans, j - i + 1)
                break

    return 0 if ans == n + 1 else ans


def minSubArrayLen2(s, nums):
    if not nums:
        return 0

    n = len(nums)
    ans = n + 1
    start, end = 0, 0
    total = 0
    while end < n:
        total += nums[end]
        while total >= s:
            ans = min(ans, end - start + 1)
            total -= nums[start]
            start += 1
        end += 1

    return 0 if ans == n + 1 else ans





if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    # nums = [0,1]
    # moveZeroes2(nums)
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    nums =[2,7,11,15]
    print(twoSum(nums,9))
