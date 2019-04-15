# -*- coding: utf-8 -*-
p='abbcabcaabbcaa'
t='abcaa'
def gen_pnext(t):
    '''生成指针对p中个位置i的下一检查位置表，用于KMP算法'''
    j,i,m=0,1,len(t)
    pnext=[0]*m
    while i<=m-1:
        if t[i]==t[j]:
            j=j+1
            pnext[i]=j
            i=i+1
        elif j!=0 and t[i]!=t[j]:
            j=pnext[j-1]
        elif j==0:
            i=i+1
    return pnext


def matching_KMP(t,p,pnext):
    '''KMP串匹配，主函数'''
    j,i=0,0
    n,m=len(t),len(p)
    while j<n and i<m:
        if i==-1 or t[j]==p[i]:
            j,i=j+1,i+1
        else:
            j=pnext[j]
    if i==m:
        return j-i
    return -1

print(matching_KMP(matching_KMP(t,p,gen_pnext(t))))