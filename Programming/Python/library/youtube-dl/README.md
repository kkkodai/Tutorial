# 概要
- Youtubeの動画をダウンロードし放題
- 個人的にpytubeより更新頻度が高くて使い勝手が良い印象

# How to install
```
pip install youtube-dl
```

# options
** [参考記事](http://d.hatena.ne.jp/masayoshi_9a7ee/20150905/1441414821) **
- 気になったオプション、ペーストしちゃったので載せるオプションが多数
	- まだまだたくさんある

** [元記事](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#options) **
- githubにあがってます

### general
```
-h, --help 
ヘルプを表示する。
--version
プログラムのVerを表示する。
-U, --update
プログラムのupdateを実行する。
-i, --ignore-errors
ダウンロードエラーを無視する。プレイリストごとダウンロードするような時に使う。
--abort-on-error
ダウンロードエラーが発生したら以降の処理を中止する。
```
### Network Options
```
--proxy URL 一部実験的
プロキシを設定する。HTTP/HTTPS及びSOCKS。ただしSOCKSは実験的扱い。socks5://127.0.0.1:1080/のような感じで指定する。
--socket-timeout SECONDS
タイムアウトの秒数を指定。単位は秒。
--source-address IP
恐らくはクライアント側からのパケットのソースアドレス偽装。つまり--proxyと似たような機能だろう。公式の説明がシンプル過ぎて推測でしかないが。
-4, --force-ipv4
-6, --force-ipv6
IPv4, IPv6を強制それぞれ強制
```

### Geo Restriction
```
```

### Video Selection
```
--playlist-start NUMBER
--playlist-end NUMBER
例えば2を指定するとプレイリスト内の2番目の動画から処理を開始もしくは処理を終える。
--playlist-items ITEM_SPEC
--playlist-items 1-3,7,10-13のように処理するプレイリスト内の番号を指定する。
```

### Download Options
```
-r, --rate-limit LIMIT
ダウンロード速度を制限する(例 50K, 4.2M)。
```

### Filesystem Options
```
-a, --batch-file FILE
動画URLを記述したファイルを指定してまとめてダウンロードする。
--id
ファイル名を動画IDのみとする。後述の-oと併用するとconflictで停止する。
-o, --output TEMPLATE
ファイル名を指定する。使用できる変数は後述のOUTPUT TEMPLATEを参照。 ←　記事見てくれ
``` 

### Post-processing Options
```
-x, --extract-audio
動画を音声のみに変換する。
--audio-format FORMAT
音声フォーマットを指定する。best, aac, vorbis, mp3, m4a, opus, wavのいずれか。
--audio-quality QUALITY
音声変換時のクオリティを指定。VBRなら0-9、CBRなら128Kなど
--recode-video FORMAT
映像フォーマットを指定のフォーマットに変換する。
--postprocessor-args ARGS
ffmpeg/avconvに渡す引数なんだろうたぶん。
-k, --keep-video
ダウンロードした変換前のファイルを残す。
```


# How to use
** [参考記事](https://shizenkarasuzon.hatenablog.com/entry/2019/02/03/123545) **

- cmdを用いる場合
1. mp4の動画
```bash
youtube-dl 'https://www.youtube.com/watch?v=sr--GVIoluU'
```
2. mp3の動画
```bash
youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=sr--GVIoluU'
```
3. playlist一括ダウンロード（mp3音声版）
```bash
youtube-dl -x --audio-format mp3 --yes-playlist 'https://www.youtube.com/watch?v=sr--GVIoluU'
```
- 「-x --audio-format mp3 --yes-playlist」を除けばプレイリスト内の動画を一括ダウンロード

4. MP4 形式での保存
```bash
$ youtube-dl -f mp4 'https://www.youtube.com/watch?v=0E00Zuayv9Q'
``` 
4. MP3 形式での保存
```bash
$ youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=0E00Zuayv9Q'
```

5. 403errorが出た時

キャッシュを消すと治ることあり！ [記事](https://teratail.com/questions/254438)
```sh
youtube-dl --rm-cache-dir
```

コマンド押下後
```sh
Removing cache dir /Users/kodaihiyori/.cache/youtube-dl ...
```