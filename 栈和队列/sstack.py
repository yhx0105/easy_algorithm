# -*- coding: utf-8 -*-
class StackUnderflow(ValueError):  # 栈下溢（空栈访问）
    pass

class SStack():
    def __init__(self):
        self.__elems=[]

    def is_empty(self):
        return self.__elems==[]

    def top(self):
        if self.__elems==[]:
            raise StackUnderflow('in SStack.top()')
        return self.__elems[-1]

    def push(self,elem):
        self.__elems.append(elem)

    def pop(self):
        if self.__elems==[]:
            raise StackUnderflow('in SStack.pop()')
        return self.__elems.pop()

if __name__=='__main__':
    st1=SStack()

    st1.top()
    while not st1.is_empty():
        print(st1.pop())
