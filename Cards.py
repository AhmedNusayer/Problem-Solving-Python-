# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Cards

n= int(input())
s = str(input())
z=0
o=0
for i in range(len(s)):
    if s[i] == 'z':
        z=z+1
    elif s[i] == 'n':
        o=o+1
for j in range(o):
    print('1', end=' ')
for k in range(z):
    print('0', end=' ')