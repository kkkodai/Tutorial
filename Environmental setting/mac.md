# Homebrew

- なにかと使います

- XcodeをインストールすればOK
```sh
# Xcodeをインストール
xcode-select --install
```

- なおOSをアップデートするたびに**`xcode-select --install`**が必要
```sh
xcode-select --install
brew upgrade carthage
carthage update

# carthageがない場合
brew install carthage
```

