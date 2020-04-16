# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Teams Forming
    
n = int(input())
ls = list(map(int,input().split()))
ls.sort()
ans = 0
for i in range(0, len(ls)-1, 2):
    ans += ls[i+1]-ls[i]
print(ans)