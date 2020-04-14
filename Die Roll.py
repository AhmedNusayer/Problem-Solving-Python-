# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Die Roll

n,m = map(int,input().split(' '))
mx = max(n,m)
if mx==1:
    print('1/1')
elif mx==2:
    print('5/6')
elif mx==3:
    print('2/3')
elif mx==4:
    print('1/2')
elif mx==5:
    print('1/3')
else:
    print('1/6')