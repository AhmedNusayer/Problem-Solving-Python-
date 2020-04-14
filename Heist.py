# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Heist

n= int(input())
ans=0
ls = list(map(int,input().split()))
ls.sort()
for i in range(len(ls)-1):
    if ls[i+1] != ls[i]+1:
        ans = ans+ ls[i+1]-ls[i]-1
print(ans)