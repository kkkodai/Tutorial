# 動画ダウンローダー

## Outline
- pytubeとyoutube-dlがあります
- pytubeは処理内容が詳細に表示されるのが良いとかなんとか。時々youtubeの仕様変更時(?)に正規表現のmatching errorみたいなのが起こるのがネック。youtube-dlは処理が速いしcmdで色々出来る。__個人的にはyoutube-dlがオススメ__。youtubeの仕様変更の内容によっては、youtube-dlが動かないことがあるかもしれないのでpytubeの動作も覚えておくべきかと！

## Install
- どちらも`pip install`からインストール可能
	- 頻繁にアップデートが行われているので、今まで問題なく動いていたモジュールがエラーを起こした場合、まず最初に`pip install -U`でアップデートしましょう
	- ffmpegのダウンロードも必須なので、忘れずに！ homebrewでインストールします
	`brew install ffmpeg`　　[ffmpeg参考記事](https://fukatsu.tech/install-ffmpeg)


### pytube
#### _How to use_
**python内で処理**

1. [PythonでYoutubeの動画をダウンロードするまで（2017/11/30現在）](https://qiita.com/Yu-Nishi/items/f49b54e68b152786a139)
	- 音声の抜き出しはffmpeg(多分オプションがあるのでしょう、わからなかったのでffmpegで)
```python
from pytube import YouTube
YouTube('http://youtube.com/watch?v=ほげほげ').streams.first().download()
```

2. [再生リストのダウンロード](https://yotazo.hateblo.jp/entry/2018/02/14/pytubeでyoutubeのplaylistダウンロードができた)
```python
from pytube import Playlist
pl = Playlist(input("Enter YouTube List : "))
pl.download_all()
```


### youtube-dl
#### _How to use_
**cmdで処理**

**[1,2の参考記事](https://shizenkarasuzon.hatenablog.com/entry/2019/02/03/123545)**

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
