# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#between the office
 
n = int(input())
s = str(input())
f=0
sf=0
for i in range(len(s)-1):
    if s[i] == 'S' and s[i+1] == 'F':
        f=f+1
    elif s[i] == 'F' and s[i+1] == 'S':
        sf=sf+1
if f>sf:
    print("YES")
else:
    print("NO")
