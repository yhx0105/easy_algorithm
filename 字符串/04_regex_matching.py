# -*- coding: utf-8 -*-
import re
# def sumInt(fname):
#     re_int=r'\b(0|[1-9]\d*)\b'
#     inf=open(fname,encoding='gbk')
#     if inf==None:
#         return 0
#     int_list=map(int,re.findall(re_int,inf.read()))
#     s=0
#     for n in int_list:
#         s+=n
#     return s

# if __name__=='__main__':
#     print(sumInt('readme'))
text=''
file=open('readme',encoding='gb18030',errors='ignore')
for line in file:
    text=text+line
file.close()
result=re.findall('0[1-9]_',text)
print(result)
