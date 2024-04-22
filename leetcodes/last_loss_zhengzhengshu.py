# > Problem: [1539. 第 k 个缺失的正整数](https: // leetcode.cn / problems / kth - missing - positive - number / description /)
#
# [TOC]
#
# # 思路
# > 首先想到的是穷举
# # 解题方法
# > 描述你的解题方法
# 循环arr，直到找到为止
# # 复杂度
# - 时间复杂度: O(n + k)
# > 添加时间复杂度, 示例： $O(n)$
#
# - 空间复杂度: O(1)
# > 添加空间复杂度, 示例： $O(n)$



class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        i = 1
        j = 1
        output = 0
        while (True):
            if i == arr[j - 1]:  # arr中有的话跳过
                i += 1
                j += 1
                if j > len(arr):  # 如果已经超了，那就从最后一个开始数k个，也就是i+k-1，然后要减去已经数过的缺失正整数的数量，所以i+k-1-count就是最后一个缺失正整数
                    output = i + k - 1 - count
                    break
            else:
                output = i
                count += 1
                i += 1
                if count == k:
                    break
        return output
