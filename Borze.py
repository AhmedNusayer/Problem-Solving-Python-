# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Borze

s = str(input())
i=0
ans = ''
while i < len(s):
    if s[i] == '.':
        ans= ans+'0'
        i+=1
    else:
        if s[i] == '-' and s[i+1] == '.':
            ans = ans + '1'
            i+=2
        else:
            ans=ans+'2'
            i+=2
print(ans)
