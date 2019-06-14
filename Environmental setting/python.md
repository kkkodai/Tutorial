# 仮想環境作成
-  __evv,virtualenv__ を入れるのがおすすめ
- ローカルを汚さないですむ


```bash
pip install ~~
```

Macなら↑で入る

# virtualenvの使い方
### 参考
- [基本操作](https://qiita.com/H-A-L/items/5d5a2ef73be8d140bdf3)
- [基本操作その2](https://qiita.com/caad1229/items/325ca5c8ad198b0ebce7)

```bash
# 仮想環境へ
$ cd [作業ディレクトリ]
$ source bin/activate
# 終了
(PythonTest)% deactivate  
```

# 矢印キーが効かなくなった場合

[問題] なぜかpyenvのpythonの場合だけ、キーが効かない

__readline__ が上手く動作しないことが原因らしい

記事どおりにやったら、とりあえず上手くいった → https://qiita.com/hidekuro/items/546a7945b0ce566a80ee
