# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:43:24 2019

@author: an
"""

class Solution:
    def coinChange(self, coins, amount):
        '''动态规划解决，状态转移矩阵为
        f(n) = 0 if n = 0
        f(n) = min(f(n-c1), f[n-c2], ..., f[n-cn]) + 1 if n >= 1
        '''
        dp = [0 for i in range(amount+1)]
        for i in range(1, amount+1):
            pre_dp = []
            for j in coins:
                if i - j < 0:
                    continue
                else:
                    # 如果 dp[i-j]不存在，就不再放入候选状态pre_dp中
                    if dp[i-j] != -1:
                        pre_dp.append(dp[i-j])
            # 如果目前的状态为空，也就是没有之前的状态可以转换到当前的状态
            if len(pre_dp) == 0:
                dp[i] = -1
            # 在那些状态里选择一个最小的，再加上1就行
            else:
                dp[i] = min(pre_dp) + 1
        
        return dp[-1]
