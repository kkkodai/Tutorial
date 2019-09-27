# Google Colaboratory
## 概要
- Colaboratoryは、無料で使うことができ、ほとんどの主要ブラウザで動作する、設定不要のJupyterノートブック環境
- Googleが、機械学習の教育、研究用に使われることを目的に、無償提供
- __無償でGPU・TPUが提供されている(制限はあるが)__
    - 将来これが当然な時代が来るのだろうか...

## おすすめサイト
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

## ＊ 基本的な使いかた
### <GPUでpythonスクリプトを使用する場合>
#### 0. ランタイムのタイプを変更

- defaultのアクセレータではGPUが設定されてない、毎回設定する必要あり（めんどい！）

- 上のバーの __ランタイム__ をクリックし、__ランタイムのタイプを変更__ からハードウェアアクセレータを選択

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

- ファイルの入出力で苦戦するかも
    - ファイル名の前に　**gdrive/My\ Drive/gesdet_keras_Colab/** と記述する必要あり(めんどくせぇ・・・)
    - cdしても意味ありません

<br>

### <TPUでpythonスクリプトを使用する場合>
#### GPUで動いてたスクリプトを色々書き直す必要あり！
#### Point
- kerasではなくtensorflow.kerasを使う
- modelをTPU用のモデルに変換する
- TPUモデルではpredictができないので確認はCPUモデルに戻して行う

詳しくは参考URLにて笑 → [https://stealthinu.hatenadiary.jp/entry/20181006/p1](https://stealthinu.hatenadiary.jp/entry/20181006/p1)
また、tensorflowがアップデートされると書式が変わることある。最新はこっち　→ https://qiita.com/koshian2/items/9d538c7082687a3fb802

あとはTIPS.mdにGPUからの変更点書きました

<br>

## 使用した感想
### 3.45GのX_train.npyの場合、アクセレータはGPU
- 1回目&2回目&3回目: まさかの固まる
    - データが大きすぎて読み込み時にメモリに乗り切らないとか
    - ランタイムの設定で、どうやらGPUが外れてた(毎回設定する必要あんのかな)

- 4回目(GPU): 動いたー、きたぁぁぁぁぁ！！！ 
    - だが、PCおもくなり途中から動かなくなる

- 5回目: Windowsの方でもう一度試す
    - 一度ランタイム切断されるが、パソコン再起動して同じipynbを開くと処理を続けたままだった。びっくり。