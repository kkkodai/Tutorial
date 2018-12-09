# Anvil
動画内のジェスチャをアノテーションするツール

## インストール
[Anvil](http://www.anvil-software.org/#)

## 使い方
anvil起動時右上の❔マークの使用書を読むのが基本

### 色の付け方
- 色の指定はhtmlの書き方と準拠してるっぽい(16進数表現可)　[HTML,CSS　ホームページの背景色や文字色](http://www.netyasun.com/home/color.html)
- こんな感じ
```html
    <group name="gesture" >
      <track-spec name="phase" type="primary" color-attr="type">
          <attribute name="type">
              <value-el color="white">preparation</value-el>
              <value-el color="pink">pre-stroke</value-el>
              <value-el color="red">stroke</value-el>
              <value-el color="#FF00FF">post-stroke</value-el>
              <value-el color="yellow">hold</value-el>
              <value-el color="#33FFFF">retraction</value-el>
              <value-el color="green">REST</value-el>
          </attribute>
      </track-spec>
```

### その他
- たまにボーダ出なくなるけどなんで？
    - その時動画が動かなくなる？