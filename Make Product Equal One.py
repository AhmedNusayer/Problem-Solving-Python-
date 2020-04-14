# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Make product equal one

n = int(input())
ls = list(map(int,input().split()))
ans=0
p=0
m=0
m1=0
z=0
for i in range(len(ls)):
    if ls[i] > 1:
        ans = ans + ls[i]-1
        p=p+1
    elif ls[i] == -1:
        m1=m1+1
    elif ls[i] < -1:
        ans = ans + abs(ls[i]+1)
        m=m+1
    elif ls[i] == 0:
        z=z+1
if (m+m1)%2 == 0 or z > 0:
    print(ans+z)
else:
    print(ans+z+2) 