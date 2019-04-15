# -*- coding: utf-8 -*-
# l=[{'a':2,'b':2},{'a':1,'b':3}]
# def combine_dic(l):
#     if l[0]['a']==l[1]['a'] and l[0]['b']!=l[1]['b']:
#         l[0]['b'] = str(l[0]['b'])+'#'+str(l[1]['b'])
#         l = l[0]
#         return l
#     else:
#         return -1
# print(combine_dic(l))
# l.append(1)
# print(l)
# l.pop()
# print(l)
# print(l[-1])
import sys
def main(args):
    print(args)

if __name__=='__main__':
    print("执行如下代码__name__=='__main__'")
    main(sys.argv[1:])