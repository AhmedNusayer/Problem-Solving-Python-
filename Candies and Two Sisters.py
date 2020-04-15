# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Candies and two sisters
'''
import math
t = int(input())
ans = []
for i in range(t):
    n = int(input())
    if n%2 == 0:
        ans.append(int(n/2-1))
    else:
        mid = math.ceil(n/2)
        ans.append(n-mid)
for j in range(t):
    print(ans[j])