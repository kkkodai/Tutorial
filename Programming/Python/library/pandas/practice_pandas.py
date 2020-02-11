# -*- coding: utf-8 -*-
"""できない
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import matplotlib as mpl
mpl.__version__
# '1.5.0'

import numpy as np
np.__version__
# '1.10.1'

import pandas as pd
pd.__version__
# u'0.17.0'

csv = 'ambientNOxCH.csv'
df = pd.read_csv(csv, index_col=0, header=[0, 1, 2], skiprows=[0], encoding='shift-jis')
df = df.iloc[:, [0, 3, 6]]
df.columns = [u'東京', u'札幌', u'福岡']
df.index = pd.to_datetime(df.index)
df.head()
df.plot()
"""

#できた
import numpy as np
from pandas import *
from pylab import *
import matplotlib.pyplot as plt
from numpy.random import randn

# シリーズの単純なプロッティング
#s = Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
#s.plot()

#plt.savefig("image.png")
#plt.show()


#df = DataFrame(np.random.randn(10, 4).cumsum(0),
#               columns=['A','B','C','D'],
#               index=np.arange(0, 100, 10))
#df.plot()
#plt.savefig("image2.png")
#plt.show()

# シリーズを可視化する
#data = Series(np.random.randn(16), index=list('abcdefghijklmnop'))
# 縦の棒グラフ
#data.plot(kind='bar',color='k',alpha=0.1)#, ax=axes[0], color='k', alpha=0.7)
# 横の棒グラフ
#data.plot(kind='barh', ax=axes[1], color='r', alpha=0.6)

#plt.savefig("image3.png")
#plt.show()

#data.plot(kind='barh',color='k', alpha=0.6)
#plt.savefig("image4.png")
#plt.show()

# データフレームを可視化する
df = DataFrame(np.random.randn(6, 4),
               index=['1','2','3','4','5','6'],
               columns=Index(['A','B','C','D'], name='Genus'))

print( df )
# =>
# Genus         A         B         C         D
# 1     -0.350817 -0.017378 -0.991230 -0.223608
# 2      0.478712 -0.472764  0.677484 -0.852312
# 3      1.402219  0.381440  0.370080  0.682125
# 4     -1.733590  0.296124 -0.014841  1.140705
# 5      0.373399  1.150718  1.341984  1.040759
# 6     -0.013301 -0.202793 -1.367493 -0.572954

#df.plot()
#plt.savefig("image5.png")
#plt.show()


#df.plot(kind='bar',grid=False, alpha=0.8) # 棒グラフにする (grid線)
#plt.savefig("image6.png")
#plt.show()


#df.plot(kind='barh', stacked=True, alpha=0.5) # 積み上げ棒グラフにする (stacked オプション)
#plt.savefig("image7.png")
#plt.show()

df = read_csv('ambientNOxCH.csv',index_col=1) 
df = df.iloc[1:3,1:]
print(df)

df.plot()
plt.savefig("image8.png")
plt.show()