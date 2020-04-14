# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""

#New year Transportation

n,t = map(int,input().split(' '))
ls = list(map(int,input().split(' ')))
flag=0
i=0
while i<len(ls):
    #print(i+1 + ls[i])
    if i+1 + ls[i] == t:
        print("YES")
        flag = 1
    i = i+1 + ls[i] - 1 
if flag == 0:
    print("NO")
