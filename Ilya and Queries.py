# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Ilya and Queries

s = str(input())
n = int(input())
ans=[]
sm = []
tsm=0
sm.append(0)
for t in range(1,len(s)):
    if s[t] == s[t-1]:
        tsm += 1
        sm.append(tsm)
    else:
        sm.append(tsm)
#print(sm)
for i in range(n):
    a,b = map(int,input().split(' '))
    ans.append(sm[b-1] - sm[a-1])
for k in range(n):
    print(ans[k])
