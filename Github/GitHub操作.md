# 様々な場面でのgitコマンド

## 操作

### fetch 
- データをリモートからローカルに取ってくる(だけで更新はせず)

- git pull = git fetch && git merge origin/master

### 直前のコミットを取り消したい

コツ: まずはローカルを変更して、後ほどリモートを消す

```bash
git commit --amend -m "新しい内容"      # ローカル変更
git push -f origin master    # リモート変更
```

参考資料: git commit --amendでコミットメッセージを修正[https://qiita.com/piruty/items/2fbfd26fd8dcbfed592a]

### ssh接続

imacでは毎回必要

```
ssh -T github-kkkodai
```

### レポジトリを作成する

ブラウザ上のbitbucketでレポジトリを作成する
すでに誰かの作ったリポジトリを自分のPCにいれたいときは、 $ git clone git@bitbucket.org:ユーザ名/レポジトリ名.git
（bitbucketは基本的に非公開なので、管理者に教えてもらう）。

指定ディレクトリは操作ディレクトリ。
・初回
$git init
$git add -A
$git commit -m "comment"
$ git remote add origin https://github.com/<username>/レポジトリ名.git
$ git push -u origin master

・次回以降
$git add -A(Aの代わりにファイル名ならそのファイルのみ操作できる)
$git commit -m "comment"
$ git push -u origin master


git addする前に
    最初にgit pullをして、最新の状態を自分のディレクトリ（ローカルレポジトリという）に反映しておこう）


commitの後にpullをするとブランチが繋がってしまうので注意。

### ブランチ作成
ブランチ作成・変更同時に行うには -b
$ git branch -b <ブランチ名>
リモートに反映(初回のみ)
$ git add <ファイル名>
$ git commit -m “コメント”
$ git push origin <ブランチ名>
次回からは<ブランチ名>に⬇︎で反映するっぽい
$ git add <ファイル名>
$ git commit -m “コメント”
$ git push

### 複数アカウントでの操作（windows版）
- 切り替え時初回は毎回以下の操作が必要かも。
- 不便なのでもっと簡単な方法でできないものか
- 参考資料
	- [Windowsで会社用と個人用のGitHubアカウントを Httpsを使って簡単に切り替える方法を丁寧に説明する。](https://zenn.dev/longbridge/articles/a91089c30851ff#%E8%A4%87%E6%95%B0%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%A7-github-%E3%81%AB-https-%E6%8E%A5%E7%B6%9A%E3%81%99%E3%82%8B)

'''sh
~~$ git config --local credential.helper wincred~~
# リモート側のリポジトリ情報を初回addする際に使う
$ git remote add origin https://github.com/【アカウント名】/【リポジトリ名】
$ git remote origin set-url https://【アカウント名】@github.com/【アカウント名】/【リポジトリ名】

'''


## 注意点
### PCを変えて今まで作業していたレポジトリにpushする際、config設定をすること
- Authorとcommiter設定が新しいPC版になっているので、**以前のと同一にしたければ設定すること**
- じゃないと他のユーザ名やアドレスが表示されてまう

```bash
# チェック
git log -1 --pretty=full

# 変更方法
git config --global user.name onamae
git config --global user.email email@example.com

# 変更確認
git config --global --list
```

- 参考記事1（Author変更方法）https://hacknote.jp/archives/15745/
- 参考記事2（間違って1回pushしちゃった場合）：https://hacknote.jp/archives/15003/

### Github Desktopに関して
環境設定のgitに設定したユーザ名とメールアドレスが`cat ~/.gitconfig`に反映される
アカウントAでpushする際、その前にGithub Desktopのgitの設定をアカウントBのユーザ名とメールアドレスにすると、アカウントBでpushしたことになるから注意

### Sublime Mergeについて
imac上だとpushが動かないという不具合があったけども、上記の「ssh接続」の章を実行した後だとうまくいくっぽい？