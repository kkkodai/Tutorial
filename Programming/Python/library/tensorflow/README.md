# pip install tensorflow してもmacで使えない
- 色々迷走した
- pip install --ignore-installed tensorflow でOKではなかった
- sudo pip install --upgrade tensorflowでinstallはできてmoduleの認識はできた
- 下のようなErrorを吐く
```
TypeError: __init__() got an unexpected keyword argument 'serialized_options'
```

→ 現状1.10.0や1.12.0だとうまくいかん状況ということ?

## 結論
- 1.6.0以降古いCPUでは動かないとのこと
    - URL:(https://arakan-pgm-ai.hatenablog.com/entry/2018/06/21/090000)[https://arakan-pgm-ai.hatenablog.com/entry/2018/06/21/090000]
- 1.5.0入れたら治った（かも？）
