# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:40:31 2019

@author: an
"""

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        bias = 0
        label = True
        while label:
            if nums[bias] == nums[bias + 1]:
                nums.pop(bias + 1)
            else:
                bias += 1
            if bias + 1 >= len(nums):
                label = False
        return len(nums)
    
nums =  [1]

h = Solution()
r = h.removeDuplicates(nums)
print(r)