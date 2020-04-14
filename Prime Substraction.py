# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Prime Substraction

t = int(input())
ans=[]
for i in range(t):
    x,y = map(int,input().split(' '))
    if x-y == 1:
        ans.append(0)
    else:
        ans.append(1)
for j in range(t):
    if ans[j] == 0:
        print("NO")
    else:
        print("YES")