# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 09:07:51 2022

mavzu: o'yin, FizzBuzz'
"""
sonlar=list(range(1,100))
#print(sonlar)
def avto(sonlar):
    l=len(sonlar)
    avto=[]
    for i in range(l-1,-1,-1):
        if (i%3==0):
            print(i,'3 bo\'lsa FizzBuzz')
        elif i%5==0:
            print(i,'5 bo\'lsa Buzz')
        else:
            print(i,'3 va 5 bo\'lsa Fizz')
    avto.append([i])
    return avto
print(f"{avto(sonlar)}")
