# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:15:08 2019

@author: an
"""

class Solution:
    def change(self, amount, coins):
        # dp初始化，可以认为钱数为0时，组合数为1，即不使用任何零钱也是一种组合
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        # 每增加一种零钱，就更新一次状态值，就是前i种硬币构成的方法数，每次加入一种硬币
        for i in coins:
            for j in range(i, amount+1):
                dp[j] = dp[j] + dp[j - i]
        return dp[amount]