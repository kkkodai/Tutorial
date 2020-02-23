# csv
### 基本操作
- indexが列指定、colonmnが行指定
- [pandas.DataFrameに列や行を追加（assign, appendなど）](https://note.nkmk.me/python-pandas-assign-append/)
- ソート
- [pandas.DataFrame, Seriesのインデックスを振り直すreset_index](https://note.nkmk.me/python-pandas-reset-index/)
- [置換はreplace](https://note.nkmk.me/python-pandas-replace/)
- [ユニークな値の操作(個数、頻度)](https://note.nkmk.me/python-pandas-value-counts/)

#### とっても細かい話
- svmdataset作ってた時の話だけど,カラム(列)の数値が同じだとcsvからtxtにデータを移すとき、「数値.1」という形式になってしまう、これはcolumnの性質が原因か
    - columnでなければうまくいくってことか
- 具体例(9番目)
```
1 1:107.247 2:26.1255 3:107.953 4:56.716 5:85.8988 6:54.5754 7:73.085 8:83.0368 9:83.0368.1 10:99.4314 11:130.024 12:59.5407 13:132.85 14:90.1748 15:130.025 16:105.813 17:88.7692 18:122.905 19:73.7991 20:172.717 21:51.7444 22:223.926 23:116.502 24:127.859 25:113.64 26:175.568 27:105.841 28:226.071 
```
    
# pandasでの図の表示例
- `import matplotlib.pyplot as plt`を行う、`import matplotlib as plt`ではだめです

#### [正解例]
~~~python
import pandas as pd
import numpy as np
import math
import random
import matplotlib.pyplot as plt

random.seed(0)
# 乱数の係数
random_factor = 0.05
# サイクルあたりのステップ数
steps_per_cycle = 80
# 生成するサイクル数
number_of_cycles = 50

df = pd.DataFrame(np.arange(steps_per_cycle * number_of_cycles + 1), columns=["t"])
df["sin_t"] = df.t.apply(lambda x: math.sin(x * (2 * math.pi / steps_per_cycle)+ random.uniform(-1.0, +1.0) * random_factor))
df[["sin_t"]].head(steps_per_cycle * 2).plot()

plt.show()
~~~

#### [不正解]
~~~python
import pandas as pd
import numpy as np
import math
import random
import matplotlib as plt

random.seed(0)
# 乱数の係数
random_factor = 0.05
# サイクルあたりのステップ数
steps_per_cycle = 80
# 生成するサイクル数
number_of_cycles = 50

df = pd.DataFrame(np.arange(steps_per_cycle * number_of_cycles + 1), columns=["t"])
df["sin_t"] = df.t.apply(lambda x: math.sin(x * (2 * math.pi / steps_per_cycle)+ random.uniform(-1.0, +1.0) * random_factor))
df[["sin_t"]].head(steps_per_cycle * 2).plot()

plt.show()
~~~

- なお保存は下の順で行う
~~~python
df.plot()
plt.savefig("image2.png")
plt.show()
~~~

