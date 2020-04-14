# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Caisa and Pylons

n = int(input())
e=0
ls = list(map(int,input().split()))
ans = ls[0]
for i in range(len(ls)-1):
    e = e+ls[i]-ls[i+1]
    if e < 0:
        ans = ans+abs(e)
        e=0
    #print(e)
print(ans)
