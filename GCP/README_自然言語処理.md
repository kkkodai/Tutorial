# GCP:Cloud Natural Language
## 概要
- GCPで使える自然言語処理ツールみたいなもん

- 感情分析、エンティティ分析、エンティティ感情分析、公文分析、コンテンツの分類がある
    - モノによっては日本語対応していない

- 参考URL:[https://cloud.google.com/natural-language/?hl=ja](https://cloud.google.com/natural-language/?hl=ja)
    - 下の方に料金表もあるよ

# タスク[ローカルpythonで感情分析]
- GCP内でしか使えない？と一瞬不安になったがそんなことはなかった！

- python3.6を使用

## 手順
### 1. API keyの発行
- 下のurlを参考にすればOK <br>
[https://cloud.google.com/docs/authentication/api-keys?hl=ja&visit_id=636852169039360185-2394580745&rd=1#using_an_api_key](https://cloud.google.com/docs/authentication/api-keys?hl=ja&visit_id=636852169039360185-2394580745&rd=1#using_an_api_key)

    - APIは重要な情報なので、色々制限かける方が安全、僕はとりあえず発行APIで使えるAPIを制限しました

### 2. スクリプト
- チュートリアル、urlは[これ](https://to-kei.net/python/google-natural-language-api/)

```
import requests 
 
#APIキーを入力
key = "YourAPIkey"
 
#感情分析したいテキスト
text = "こんにちは、今日もいい天気ですね。明日も晴れるといいなあ。でも最近晴れてるのに寒いですよね。"
 
#APIのURL
url = 'https://language.googleapis.com/v1/documents:analyzeSentiment?key=' + key
 
#基本情報の設定 JAをENにすれば英語のテキストを解析可能
header = {'Content-Type': 'application/json'}
body = {
    "document": {
        "type": "PLAIN_TEXT",
        "language": "JA",
        "content": text
    },
    "encodingType": "UTF8"
}
 
#json形式で結果を受け取る。
response = requests.post(url, headers=header, json=body).json()
 
#分析の結果をコンソール画面で見やすく表示
print("総合magnitude:",response["documentSentiment"]["magnitude"])
print("総合score:",response["documentSentiment"]["score"])
for i in response["sentences"]:
    print(i["text"]["content"],"magnitude:",i["sentiment"]["magnitude"],", score:",i["sentiment"]["score"])
```
