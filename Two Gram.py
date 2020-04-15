# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Two Gram

n = int(input())
s = str(input())
ls = []
index = []
mx=0
for i in range((len(s)-1)):
    ls.append(s[i]+s[i+1])
    #ls[i] = s[i] + s[i+1]
    index.append(0)
for i in range(len(ls)):
    j=i+1
    for j in range(len(ls)):
        if ls[i] == ls[j]:
            index[i] = index[i] + 1
            if index[i] > mx:
                mx = index[i]
            
#print(ls)
#print(index)    
print(ls[index.index(mx)])