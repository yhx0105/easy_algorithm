# -*- coding: utf-8 -*-
class StackUnderflow(ValueError):  # 栈下溢（空栈访问）
    pass

class LNode(object):
    '''节点'''
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class LStack():
    def __init__(self):
        self.__top=None

    def is_empty(self):
        return self.__top is None

    def top(self):
        if self.is_empty():
            raise StackUnderflow('in LStack.top()')
        return self.__top.elem

    def push(self,elem):
        lnode=LNode(elem)
        lnode.next=self.__top
        self.__top=lnode


    def pop(self):
        if self.__top is None:
            raise StackUnderflow('in LStack.pop()')
        p=self.__top
        self.__top=p.next
        return p.elem

if __name__=='__main__':
    st1=LStack()
    st1.push(1)
    st1.push(2)
    st1.top()
    while not st1.is_empty():
        print(st1.pop())