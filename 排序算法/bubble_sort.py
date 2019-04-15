# -*- coding: utf-8 -*-
def bubble_sort(text):
    '''冒泡排序'''
    n=len(text)
    for i in range(n-1):
        '''遍历次数'''
        found=False
        for j in range(0,n-1-i):
            '''内层的比较'''
            if text[j]>text[j+1]:
                text[j],text[j+1]=text[j+1],text[j]
                found=True
        if not found:
            break
    return text


if __name__=='__main__':
    text=[1,2,4,3,5]
    print(text)
    print(bubble_sort(text))

