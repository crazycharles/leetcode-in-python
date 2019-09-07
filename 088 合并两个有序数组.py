# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 17:08:11 2019

@author: an
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur1 = m - 1
        cur2 = n - 1
        p = m + n - 1
        #双指针法
        # cur1是第一个数组的指针，从第一个数组最后一个数开始比较
        # cur2是第二个数组的指针，从第二个数组最后一个数开始比较
        # p 是第三个指针，从 m+n-1位置依次向前，代表的是要插入的位置
        # cur1与cur2依次比较大小，大的数插入到位置p
        while cur1 >= 0 and cur2 >= 0:
            if nums1[cur1] < nums2[cur2]:
                nums1[p] = nums2[cur2]
                cur2 -= 1
                p -= 1
            else:
                nums1[p] = nums1[cur1]
                cur1 -= 1
                p -= 1
        #判断第二个数组是否被比较完成，
        #否则在第一个指针走到头但第二个指针没有走到头的情况下，把第二个数组的值依次放入第一个数组中
        while cur2 >= 0:
            nums1[p] = nums2[cur2]
            cur2 -= 1
            p -= 1
        return nums1
