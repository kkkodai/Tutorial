# chmod

- [参考URL](https://www.k-tanaka.net/unix/chmod.php)

# history

# find
ファイル名がわかっているけどディレクトリの位置が分からないとき、findコマンド(mac/linux)、もしくはmdfindコマンド(macのみ)、locateコマンド(linuxのみ)を使用します。 

# du
### duコマンドを使用してMacの5GB以上のフォルダを確認
[参考url](https://qiita.com/twipg/items/4cf763aa0a09ca1e387f)
```sh
sudo du -g -x -d 5 / | awk '$1 >= 5{print}'
```
### メガ表示
```sh
$ du -sh [ディレクトリ名]
```

# touch
### ファイル大量作成
1. [その１](http://kazmax.zpp.jp/linux/bash_tips.html)
```sh
$ touch foo_{1..30}.txt
```
2. [その２](https://saratoga.jp/tips/457)
```sh 
$ n=1; while [ ${n} -le 5 ] ; do echo "ABCDEFGHIJKLMNOPQRSTUVWXYZ" > ${n}.txt; n=`expr $n + 1`; done
```
3. [その３](https://masawada.hatenablog.jp/entry/2015/03/03/203313)
うまくいかない
```sh
for i in {1..1000}; do dd if=/home2 of=temp_${i} bs=1k count=1 ; done
```

# 省略コマンド(エイリアスとかのこと？)
```bash
$ sudo vim ~/.bashrc　　(or sudo vim /etc/profile)

$ source ~/.bashrc　　(or source /etc/profile)
```
- 情報を統制したいので/etc/profileに記述するのではなくて、bashrcに書きましょう

- 注意)source .bash_profileは上手くいかなんだ

