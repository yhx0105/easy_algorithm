# -*- coding: utf-8 -*-
from 栈和队列 import sstack

def check_parens(text):
    '''括号配对检查函数，text是被检查的字符串'''
    parens='()[]{}'
    open_parens='([{'
    opposite={')':'(',']':'[','}':'{'}

    def parenthese(text):
        '''括号生成器，每次调用返回text里的下一个括号及其位置'''
        i,text_len=0,len(text)
        while True:
            while i<text_len and text[i] not in parens:
                i+=1
                if i>=text_len:
                    return
                yield text[i],i
                i+=1


