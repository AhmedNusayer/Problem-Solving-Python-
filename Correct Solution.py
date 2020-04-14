# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:49:31 2020

@author: User
"""
#Correct solution

s = str(input())
a = str(input())
ans=''
x = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
for i in range(len(s)):
    n = int(s[i])
    x[int(n)] += 1
k=0
l=0
flag=0
f2=0
for j in range(1,10):
    if x[j] != 0:
        for k in range(x[j]):
            if f2 == 0:
                flag = 1
            ans=ans+str(j)
            if flag == 1:
                f2=1
                flag=0
                for l in range(x[0]):
                    ans=ans+'0'
            #print(j,end='')
    #print(ans)
if ans == '':
    ans = s
if ans == a:
    print("OK")
else:
    print("WRONG_ANSWER")




