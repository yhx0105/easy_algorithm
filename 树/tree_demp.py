# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, item):
        self.elem = item
        self.rchild = None
        self.lchild = None


class Tree(object):
    '''二叉树'''

    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        '''广度遍历'''
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def pre_order(self,node):
        '''先序遍历'''
        if node is None:
            return
        print(node.elem,end=' ')
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def in_order(self,node):
        '''中序遍历'''
        if node is None:
            return
        self.in_order(node.lchild)
        print(node.elem, end=' ')
        self.in_order(node.rchild)

    def pos_order(self,node):
        '''后序遍历'''
        if node is None:
            return
        self.pos_order(node.lchild)
        self.pos_order(node.rchild)
        print(node.elem, end=' ')

if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    tree.pre_order(tree.root)
    print('/n')
    tree.in_order(tree.root)
    print('/n')
    tree.pos_order(tree.root)