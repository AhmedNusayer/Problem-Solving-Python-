# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Repeating Cipher
    
n = int(input())
s = str(input())
i=0
j=1
while i < len(s):
    print(s[i],end='')
    i = i+j
    j += 1