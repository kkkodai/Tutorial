# Google Colaboratory
### 概要
- Colaboratoryは、無料で使うことができ、ほとんどの主要ブラウザで動作する、設定不要のJupyterノートブック環境
- Googleが、機械学習の教育、研究用に使われることを目的に、無償提供
- __無償でGPU・TPUが提供されている(制限はあるが)__
    - 将来これが当然な時代が来るのだろうか...

### おすすめサイト
- 基本的なルールとか確認したければこのサイト
    - url:[https://qiita.com/tomo_makes/items/b3c60b10f7b25a0a5935](https://qiita.com/tomo_makes/items/b3c60b10f7b25a0a5935)
    - 内容が多く途中で飽きるかも

- 初心者向けはこのサイトかも
    - url:[https://qiita.com/kouki_outstand/items/cd24dccbaa92274be39e](https://qiita.com/kouki_outstand/items/cd24dccbaa92274be39e)

- ファイルのアップロードは面倒とのことなので、サイト探した
    - url1:[https://qiita.com/uni-3/items/201aaa2708260cc790b8](https://qiita.com/uni-3/items/201aaa2708260cc790b8)
    - メインはこっち
    - url2:[https://qiita.com/kikuchi_kentaro/items/65be0cf40ac61849d841](https://qiita.com/kikuchi_kentaro/items/65be0cf40ac61849d841)
    - 情報補完する際こっちも閲覧

### 基本的な使いかた
#### pythonスクリプトを使用する場合
#### 1. マウント
```
from google.colab import drive
drive.mount('/content/gdrive')
```

- 表示されるURLで得た暗号鍵を打ち込む

#### 2. 実行
```
%run gdrive/My\ Drive/gesdet_keras_Colab/train_blstm_debug.py gdrive/My\ Drive/gesdet_keras_Colab/model_test.hdf5 2 gdrive/My\ Drive/gesdet_keras_Colab/dataset
```

- ファイルの入出力でで苦戦するかも
ファイル名の前に　**gdrive/My\ Drive/gesdet_keras_Colab/** と記述する必要あり(めんどくせぇ・・・)


### 使用した感想
- 後日更新
