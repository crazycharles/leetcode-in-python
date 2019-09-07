# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 20:02:17 2019

@author: an
"""

class Solution:
    def mincostTickets(self, days, costs):
        # 这里加上30天空白是为了后面求最小值时不用一个一个判断特殊情况
        # 这里的dp[i]表示的是旅行到第i天，所花费的最小金额
        dp = [0 for i in range(365 + 30 + 1)]
        for i in range(31, 365 + 30 + 1):
            if i - 30 not in days:
                # 如果今天没有行程，那么今天的花费就是昨天的花费，没有买任何火车票
                dp[i] = dp[i-1]
            else:
                #如果今天有行程的话，解决今天旅行问题的办法有三种，即买日票，周票，月票，但是买票，要从之前开始买，直到包含今天，并且今天是火车票包含的最后一天
                #比方说，今天是旅行的第8天，如果买周票的话，第2天买周票，那么刚好包含的第8天，那么dp[8] = dp[8-7] + costs[1]
                #所以就是三种买票方式中，最小花费的那一种。
                cost_lst = [dp[i-1] + costs[0], dp[i-7] + costs[1], dp[i-30] + costs[2]]
                dp[i] = min(cost_lst)
        return dp[-1]          