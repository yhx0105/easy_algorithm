# -*- coding: utf-8 -*-
class Node(object):
    '''定义节点'''

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class Single_cycle_list(object):
    '''定义单向循环列表'''

    def __init__(self, node=None):
        self._head = node
        if node:
            node.next = node

    def is_empty(self):
        return self._head == None

    def length(self):
        '''长度'''
        cur = self._head
        count = 1
        if self.is_empty():
            count = 0
        else:
            while cur.next != self._head:
                count += 1
                cur = cur.next
        return count

    def travel(self):
        '''遍历'''
        cur = self._head
        if self.is_empty():
            return None
        while cur.next != self._head:
            print(cur.elem, end=' ')
            cur = cur.next
        '''退出循环，手动打印尾节点'''
        print(cur.elem)

    def add(self, item):
        '''在首位添加元素'''
        cur = self._head
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            cur.next = self._head

    def append(self, item):
        '''尾部插入'''
        cur = self._head
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    def insert(self, pos, item):
        '''任意位置插入节点'''
        pre = self._head
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append()
        else:
            for i in range(pos - 1):
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def search(self, item):
        '''查找'''
        cur = self._head
        while cur.next != self._head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False
        if self.length == 0:
            return False

    def remove(self, item):
        '''删除'''
        cur = self._head
        pre = None
        while cur.next != self._head:
            if cur.elem == item:
                if cur == self._head:
                 # 头节点情况
                    rear=self._head
                    while rear.next!=self._head:
                        rear=rear.next
                    self._head=cur.next
                    rear.next=self._head
                else:
                    pre.next = cur.next
                    break
            else:
                pre = cur
                cur = cur.next
        # 退出循环，代表尾节点
        if cur.elem == item:
            if cur==self._head:
                #只有一个节点
                self._head=None
            else:
                pre.next = cur.next
        if self.is_empty():
            return False



if __name__ == "__main__":
    li = Single_cycle_list()
    print(li.is_empty())
    print(li.length())
    li.append(1)
    li.add(4)
    li.add(2)
    li.travel()
