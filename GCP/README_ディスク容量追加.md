# [add disk strage](https://qiita.com/uni-3/items/30309beec07bbc5e8944)

gceを使ってるとインスタンスの容量が足りなくなることがある

google compute engineディスクの容量を増やす方法を試した

## 方法
- サイトを見ようwよく纏まってる

### gceインスタンスでマウントボリュームの設定

__なぜか自分の場合ではこの設定をする必要がなかった(作りたてのインスタンスに追加したから？)__

__下の感じになるらしいです__

```
# ディスクのサイズが設定した値
$ sudo lsblk
# パーティションサイズを拡大
$ sudo growpart /dev/sda 1
CHANGED: partition=1 start=2048 old: size=62912479 end=62914527 new: size=536868831,end=536870879
# ディスク容量を拡張する
$ sudo resize2fs /dev/sda1
```

