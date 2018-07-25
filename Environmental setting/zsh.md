# zsh編
macユーザならシェルはデフォルトのbashよりもzshの方が何かと便利(らしい)、それと見た目かっこいい..！


- 参考サイト
1. この通りやればOK→[macのシェルをbashからzshに変更してPreztoを適用する](https://qiita.com/taktakfu/items/ce228762c9078466c71f)

2. 最速はこれかな→[ミニマムな.zshrc](http://yuk.hatenablog.com/entry/2014/09/09/014115)

一応自分がどのようにやったかメモ（1を部分的に行ったらほぼ2の通りになったので2がおすすめ？）


```sh
$ brew install zsh
$ sudo vi /etc/shells
# List of acceptable shells for chpass(1).
# Ftpd will not allow users to connect who are not using
# one of these shells.

/bin/bash
/bin/csh
/bin/ksh
/bin/sh
/bin/tcsh
/bin/zsh
/usr/local/bin/zsh    # この行を追加
chsh -s /usr/local/bin/zsh  # ログインシェルをbashからzshに変更
```

### ターミナル再起動後
警告が表示されるが気にせずq押して画面閉じる
```sh
# これ、自分はしなかった、bash_profileぶっ壊れているので
$ cat ~/.bash_profile >> ~/.zshrc
# インストール
$ git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"

# ~/.zshrcのバックアップ
# 次の手順で~/.zshrcファイルを作成するため。(自分はしなかった)
$ mv ~/.zshrc ~/.zshrc_old

# Preztoの設定ファイル作成
$ setopt EXTENDED_GLOB
for rcfile in "${ZDOTDIR:-$HOME}"/.zprezto/runcoms/^README.md(.N); do
  ln -s "$rcfile" "${ZDOTDIR:-$HOME}/.${rcfile:t}"
done

# 一時退避しておいた~/.zshrcの内容を、上記で作成された設定ファイルに追記(なお自分はしなかった)
$ cat ~/.zshrc_old >>  ~/.zshrc
```
### 完成、ターミナル再起動後かっこよくなってます
なお、bashに戻すには
```sh
chsh -s /bin/bash
```