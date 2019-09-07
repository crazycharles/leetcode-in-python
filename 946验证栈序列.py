# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 16:29:08 2019

@author: an
"""

class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        j = 0
        # 模拟栈的过程
        for i in pushed:
            stack.append(i)
            # 如果加入的元素恰好等于出栈的元素，就一直弹出
            while stack and j < len(popped) and popped[j] == stack[-1]:
                stack.pop()
                j += 1
        if len(stack) == 0:
            return True
        else:
            return False