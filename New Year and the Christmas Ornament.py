# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#New Year and the Christmas Ornament

y,b,r = map(int,input().split(' '))
if r>b+1:
    r=b+1
else:
   b=r-1
if y>=r or y>=b:
    y=b-1
else:
    b=y+1
    r=b+1
print(b+r+y)