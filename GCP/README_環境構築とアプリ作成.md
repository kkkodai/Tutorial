# Making Server
## 概要
- サーバーを立ち上げたい！！

- ローカルからssh！！

## 手順

- __基本、[このサイト](https://www.topgate.co.jp/gcp03-google-compute-engine-launch-instance)が参考になります！__
    - ただし,gcloudのインストールは他のサイトを参考にした

### 1. インスタンスを立ち上げる


### 2. cloud SDKのインストール
- __gcloudのインストールをしたい__

- よくあるサイトからインストールしてsh実行はうまくいかなかった..
    - ナンデダ...

- 下ならできた！
    - [参考サイト](https://qiita.com/sakamossan/items/8ff74ed377dc77325b80)


```
$ brew cask install google-cloud-sdk
```

### 3. gcloudの設定

- ログイン認証を求められる、ブラウザ移動
```
gcloud init
```

- プロジェクト、リージョン、ゾーンの設定をするか聞かれる　> 今回はしてみた

```bash
You are logged in as: [hiyorikodai@gmail.com].

Pick cloud project to use: 
 [1] disco-aegis-231109
 [2] quick-country-230916
 [3] Create a new project
Please enter numeric choice or text value (must exactly match list 
# 回答箇所
item):  1         

Your current project has been set to: [disco-aegis-231109].

Do you want to configure a default Compute Region and Zone? (Y/n)?  Y

Which Google Compute Engine zone would you like to use as project 
default?
If you do not specify a zone via a command line flag while working 
with Compute Engine resources, the default is assumed.
 [1] us-east1-b
 [2] us-east1-c
 [3] us-east1-d
 [4] us-east4-c
 [5] us-east4-b
 [6] us-east4-a
 [7] us-central1-c
 [8] us-central1-a
 [9] us-central1-f
 [10] us-central1-b
 [11] us-west1-b
 [12] us-west1-c
 [13] us-west1-a
 [14] europe-west4-a
 [15] europe-west4-b
 [16] europe-west4-c
 [17] europe-west1-b
 [18] europe-west1-d
 [19] europe-west1-c
 [20] europe-west3-c
 [21] europe-west3-a
 [22] europe-west3-b
 [23] europe-west2-c
 [24] europe-west2-b
 [25] europe-west2-a
 [26] asia-east1-b
 [27] asia-east1-a
 [28] asia-east1-c
 [29] asia-southeast1-b
 [30] asia-southeast1-a
 [31] asia-southeast1-c
 [32] asia-northeast1-b
 [33] asia-northeast1-c
 [34] asia-northeast1-a
 [35] asia-south1-c
 [36] asia-south1-b
 [37] asia-south1-a
 [38] australia-southeast1-b
 [39] australia-southeast1-c
 [40] australia-southeast1-a
 [41] southamerica-east1-b
 [42] southamerica-east1-c
 [43] southamerica-east1-a
 [44] asia-east2-a
 [45] asia-east2-b
 [46] asia-east2-c
 [47] europe-north1-a
 [48] europe-north1-b
 [49] europe-north1-c
 [50] northamerica-northeast1-a
Did not print [6] options.
Too many options [56]. Enter "list" at prompt to print choices fully.
Please enter numeric choice or text value (must exactly match list 

# 回答箇所
item):  34

Your project default Compute Engine zone has been set to [asia-northeast1-a].
You can change it by running [gcloud config set compute/zone NAME].

Your project default Compute Engine region has been set to [asia-northeast1].
You can change it by running [gcloud config set compute/region NAME].

Created a default .boto configuration file at [/Users/kodaihiyori/.boto]. See this file and
[https://cloud.google.com/storage/docs/gsutil/commands/config] for more
information about configuring Google Cloud Storage.
Your Google Cloud SDK is configured and ready to use!

* Commands that require authentication will use hiyorikodai@gmail.com by default
* Commands will reference project `disco-aegis-231109` by default
* Compute Engine commands will use region `asia-northeast1` by default
* Compute Engine commands will use zone `asia-northeast1-a` by default

Run `gcloud help config` to learn how to change individual settings

This gcloud configuration is called [default]. You can create additional configurations if you work with multiple accounts and/or projects.
Run `gcloud topic configurations` to learn more.

Some things to try next:

* Run `gcloud --help` to see the Cloud Platform services you can interact with. And run `gcloud help COMMAND` to get help on any gcloud command.
* Run `gcloud topic --help` to learn about advanced features of the SDK like arg files and output formatting
~/Downloads ❯❯❯ 
```

- [サイト](https://www.topgate.co.jp/gcp03-google-compute-engine-launch-instance)ではCUIの操作で上記の内容を行なっている

### 4. ssh操作
- VMインスタンスのページの接続の見出しの下にある引き出しをクリックすると、「gcloudコマンドを表示」があり、これをクリックしたときに表示されるコマンドラインをコピペ

- こんなかんじになる
```
gcloud compute --project "disco-aegis-231109" ssh --zone  <instance-zone> <instance-name>
```


- 次に鍵の設定、ローカルpc内の鍵を使えた？秘密鍵と公開鍵のどちらを使ったのかよくわかっていない(下手して俺どちらも一緒...？)
    - ここら辺理解できていない、やばいよなぁ


__接続できた！！！__

# アプリ作り
- .yamlが重要

- 下記のコマンドを実行すれば、とりあえず更新&動作する

```bash
# 更新
gcloud app deploy
# 動作
gcloud app browse
```