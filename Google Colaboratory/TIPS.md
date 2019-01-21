# TIPS

## ＊ GPUで作成したモデルを利用する際に注意すること
- エラー内容: kerasのバージョンが2.0.9ではモデルの読み込みでKeyError: 0が発生した

- 解決法: __kerasのバージョンを2.2.0以上にする__

- 参考url:[https://blog.shikoan.com/keras-load-model-from-colab/](https://blog.shikoan.com/keras-load-model-from-colab/)

焦ったぁぁ

## ＊ TPU使用する際の変更点

### 脳死でkerasをtensorflow.kerasに変更すればOKではない！

- モジュールはtensorflowに対応したものにする
    - ここを参考に描き直しましょう → [https://www.tensorflow.org/api_docs/python/tf/keras/layers](https://www.tensorflow.org/api_docs/python/tf/keras/layers)
    - keras.layers.recurrentとかkeras.layers.wrappersはtensorflow.keras.layersにする

### 実行してもTPUが使われてないことがある

- 実行時に上の表示あるかをチェック
```
INFO:tensorflow:Querying Tensorflow master (b'grpc://10.8.107.202:8470') for TPU system metadata.
INFO:tensorflow:Found TPU system:
```

- 最初全然動かなかったが(CPUしか使えなかった)下記の順にmodelを構築したらうまくいった(?)

```python
    # 1.Compile
    model.compile(
        optimizer=tf.train.AdamOptimizer(learning_rate=1e-3, ),
        loss="categorical_crossentropy",
        metrics=['accuracy']
    )

    # 2.TPU用のおまじない
    tpu_model = tf.contrib.tpu.keras_to_tpu_model(
    model,
    strategy=tf.contrib.tpu.TPUDistributionStrategy(
        tf.contrib.cluster_resolver.TPUClusterResolver(tpu='grpc://' + os.environ['COLAB_TPU_ADDR'])
        )
    )

    # 3.fit
    history = History()
    hist = tpu_model.fit(X_train, Y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, validation_data=(X_validation, Y_validation),callbacks=[history])
```

- keras時に使用したevaluationは使えなかった <- error吐いた

## ファイルが存在するのに動かない
- 同ファイル名で上書き保存すると、(1)というのがついてしまうことがある
    - 同期してたらだいじょうぶなはずだが

## Google driveと連携するには

## ファイルのアップロード