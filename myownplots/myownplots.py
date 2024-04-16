#!/usr/bin/env python3
import matplotlib.pyplot as plt
import random
from myownplots.exceptions import WrongArgsError,DifferentLengthArgsError
def create_plot(arg1,arg2="Empty"):
    if not(isinstance(arg1,list)):
        raise WrongArgsError
    if not(isinstance(arg2,list)) and arg2!="Empty":
        raise WrongArgsError
    if arg2!="Empty" and len(arg1)!=len(arg2):
        raise DifferentLengthArgsError
    for i in range(len(arg1)):
        if not(isinstance(arg1[i],int)):
            raise WrongArgsError
        if arg2!="Empty" and not(isinstance(arg2[i],int)):
            raise WrongArgsError
    if arg2=="Empty":
        arg2=[]
        for i in range(len(arg1)):
            arg2.append(i)
    plt.plot(arg2, arg1)
    plt.show()

def create_random_plot(n):
    if not(isinstance(n,int)):
        raise WrongArgsError
    arg1=[]
    for i in range(n):
        arg1.append(random.randint(1,20))
    arg2=[]
    for i in range(n):
        arg2.append(random.randint(1,20))
    plt.plot(arg2, arg1)
    plt.show()
