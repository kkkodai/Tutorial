# bash編
### MACのターミナルで最初のコンピュータ名・ユーザ名を消す
bash_rcに以下の文を追記

```sh
PS1="\W $ "
```

再起動後も変更を維持するためsource .bash_profileかsource /etc/profileする（何故か手元のmacではsource .bash_profileが出来ない）
→ なお、sourceするファイルにはsource .bashrcと記述されてある必要あり

- 参考サイト：[Macのターミナルで最初のコンピューター名・ユーザー名を消す](https://tech.qookie.jp/posts/terminal-turn-off-prompt/)

### 最初のコンピュータ名・ユーザ名の色指定
\[\033[31m\]と\[\033[0m\]で囲む
```sh
$ PS1="\[\033[31m\]\u:\t \W $\[\033[0m\]"
```

