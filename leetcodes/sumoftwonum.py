class sum_of_two_num(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #  用快速排序的思想 每次进行加和比较 可以只进行一重循环 不过需要保证整数序列有序
        a = list(nums)
        a.sort()
        print(a)  # 使用临时变量对输入的数据进行操作
        i=0
        j=len(nums)-1  #添加的左右（头尾）指针
        result = []  
        for k in range(len(nums)):
            print("step ", (k + 1), "left= ", a[i], "right= ", a[j])
            if a[i] + a[j] == target:
                result= [a[i],a[j]]
                break
            if a[i] + a[j] > target: # 一前一后之和大于目标值 尾指针左移
                j -= 1
            elif a[i] + a[j] < target: # 小于则头指针右移
                i += 1
            if j == i: # 两个指针相遇  说明没找到
               result = None
               break
        if result == None:
            return None
        left = nums.index(result[0])
        if result[0]==result[1]:
            right = nums.index(result[1], left + 1)  # 要匹配列表中的第二个元素下标 就把搜索区间定位到第一个元素下标之后即可
        else:
            right = nums.index(result[1])
        return [left,right]

class sum_of_two_num_cycle(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 常规循环方法测试
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
 #以下是测试用例
a = [-1,-2,-3,-4,-5]
b = sum_of_two_num()
result = b.twoSum(a,-8)
c = sum_of_two_num_cycle()
result1 =  c.twoSum1(a,-8)
print(result)
print(result1)



