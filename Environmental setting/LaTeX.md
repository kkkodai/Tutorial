# LaTeX環境構築

- LaTeXはなにかと使います

- 基本、この[記事](https://qiita.com/DaiHasegawa/items/22732ca7a84bd34de923)を参照すればおｋ
	- ~~ただ私は上手く環境構築できず‥~~
	- MaCTeXをコマンドラインからインストールするのではなくて、[公式サイト](http://www.tug.org/mactex/mactex-download.html)からインストールしよう(たぶんそれで解決)


## 下は上手くいかず苦労した後の残骸です、一応残しておきます(まじで時間の無駄だった)↓↓↓↓↓↓↓↓↓↓
### アクション1
- **詰まったときの解決法です。参考にしてみてください** → [この記事です](https://blog.ashija.net/2017/09/08/post-916/#Skim)
	- この記事もいろいろしなくちゃいけなくてめんどくさいし、途中で詰まる
	- `sudo zsh -c "rm ./CIDFont/*(@) ./CIDFSubst/*(@)"`で`zsh:1: no matches found: ./CIDFont/*(@)`というエラーを吐き、作業がストップした


### アクション2
- __1: 記事通りしたのに、pdf出力されない！__
- pdf出力に必要なghostscriptとimagemagickをbrewでインストール
```sh
brew install ghostscript
brew install imagemagick
```

- [参考](http://teru0rc4.hatenablog.com/entry/2017/01/28/213102)

**しかし‥、imagemagickと関連するモジュールのpythonが入らねぇ！**

- __2: macOSをアップデート後、Xcodeの再インストールをしていない！__
- これしましょう
```sh
xcode-select --install
brew upgrade carthage
carthage update
```

- [参考](https://qiita.com/y-some/items/00908eadf6845020e361)

- pythonのlinkエラー出るかも
	- その際は[これ](https://qiita.com/Jung0/items/d4012814e6fb1b694208)

→ **brew install imagemagick**に成功


# LaTeX記事
### おすすめ記事をいくつか紹介
1. 知っておくといいこと [記事](https://qiita.com/Tats_U_/items/01d48eb70a8b359b0d95)

### 感想
- Qiitaさいこー