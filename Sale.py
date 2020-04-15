# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Sale

n,m = map(int,input().split(' '))
ls = list(map(int,input().split()))
ls.sort()
sm = 0
for i in range(m):
    if ls[i] < 0:
        sm = sm+(ls[i]*-1)
print(sm)
