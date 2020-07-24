#!/usr/bin/env python
# coding=utf-8
'''
@Author: John
@Email: johnjim0816@gmail.com
@Date: 2020-07-21 09:46:44
@LastEditor: John
@LastEditTime: 2020-07-21 09:47:20
@Discription: 
@Environment: python 3.7.7
'''
# Source : https://leetcode.com/problems/first-bad-version/
# Author : JohnJim0816
# Date   : 2020-07-21

##################################################################################################### 
#
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the 
# latest version of your product fails the quality check. Since each version is developed based on 
# the previous version, all the versions after a bad version are also bad.
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes 
# all the following ones to be bad.
# 
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement 
# a function to find the first bad version. You should minimize the number of calls to the API.
# 
# Example:
# 
# Given n = 5, and version = 4 is the first bad version.
# 
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# 
# Then 4 is the first bad version. 
# 
#####################################################################################################

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int n>1
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left