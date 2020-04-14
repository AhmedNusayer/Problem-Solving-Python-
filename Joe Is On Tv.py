# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Joe is on tv

n = int(input())
sm = 0
i=1
for i in range(1,n+1):
    sm = float(sm)+ float(1/i)
print(sm)