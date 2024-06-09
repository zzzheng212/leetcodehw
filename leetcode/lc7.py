from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1  # 返回唯一元素的個數


# 測試例子
solution = Solution()
nums = [1, 1, 2]
k = solution.removeDuplicates(nums)
print(k)  # 輸出: 2
print(nums[:k])  # 輸出: [1, 2]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = solution.removeDuplicates(nums)
print(k)  # 輸出: 5
print(nums[:k])  # 輸出: [0, 1, 2, 3, 4]
