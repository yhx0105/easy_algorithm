# -*- coding: utf-8 -*-
# def fabonacci(max):
#     n,a,b=0,0,1
#     l=[]
#     while n<max:
#         l.append(b)
#         a,b=b,a+b
#         n=n+1
#     return l
def fabonacci(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1




if __name__=='__main__':
    for n in fabonacci(5):
        print(n)