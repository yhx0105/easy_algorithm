# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data=pd.DataFrame(np.random.randn(1000,4),
                      index=np.arange(1000),
                      columns=list('ABCD'))
    data=data.cumsum()
    data.plot.scatter(x='A',y='B')
    plt.show()
