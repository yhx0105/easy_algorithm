# -*- coding: utf-8 -*-
import numpy as np




if __name__=='__main__':
    a=np.arange(4)
    b=a.copy()
    c=a
    d=b
    a[0]=12
    print(a)
    print(b)
    print(c)
    print(d)