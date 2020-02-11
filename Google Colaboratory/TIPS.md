# TIPS

## ＊ GPUで作成したモデルを利用する際に注意すること
- エラー内容: kerasのバージョンが2.0.9ではモデルの読み込みでKeyError: 0が発生した

- 解決法: __kerasのバージョンを2.2.0以上にする__

- 参考url:[https://blog.shikoan.com/keras-load-model-from-colab/](https://blog.shikoan.com/keras-load-model-from-colab/)

焦ったぁぁ

## ＊ TPU使用する際の変更点

### tensorflowのバージョンアップの影響をめちゃくちゃ受ける！
- 1.13から1.14にアップグレートした際、結構記法に変更があった。詳しくは → https://qiita.com/koshian2/items/9d538c7082687a3fb802
	- 記事通りにやればおけ。**神記事**

### 脳死でkerasをtensorflow.kerasに変更すればOKではない！

- モジュールはtensorflowに対応したものにする
    - ここを参考に描き直しましょう → [https://www.tensorflow.org/api_docs/python/tf/keras/layers](https://www.tensorflow.org/api_docs/python/tf/keras/layers)
    - keras.layers.recurrentとかkeras.layers.wrappersはtensorflow.keras.layersにする


### tensorflow1.14ver の挑戦（動かない）
```python

    # TPU部分
    tpu_grpc_url = "grpc://"+os.environ["COLAB_TPU_ADDR"]
    tpu_cluster_resolver = tf.contrib.cluster_resolver.TPUClusterResolver(tpu_grpc_url)
    tf.contrib.distribute.initialize_tpu_system(tpu_cluster_resolver)
    strategy = tf.contrib.distribute.TPUStrategy(tpu_cluster_resolver, steps_per_run=100)
    with strategy.scope():
        model = create_network()
        print(model.summary())
        optimizer1 = Adam(lr=0.001, beta_1=0.9, beta_2=0.999)
        # optimizer2 = Adadelta(lr=1.0, rho=0.95, epsilon=None, decay=0.0)
        # model.compile(loss='mean_squared_error', optimizer=optimizer1)
        model.compile(loss=['mean_squared_error','binary_crossentropy'], optimizer=optimizer1)
        # model.compile(keras.optimizers.SGD(0.1, momentum=0.9), "categorical_crossentropy", ["acc"])
        # hist = model.fit(X_train, Y_train_motion, batch_size=BATCH_SIZE, 
        #     epochs=EPOCHS, steps_per_epoch=X_train.shape[0] // BATCH_SIZE, validation_steps=X_validation.shape[0] // BATCH_SIZE,
        #     validation_data=(X_validation, Y_valid_motion))
        hist = model.fit(X_train, [Y_train_motion,Y_train_phase], batch_size=BATCH_SIZE, 
            epochs=EPOCHS, steps_per_epoch=X_train.shape[0] // BATCH_SIZE, validation_steps=X_validation.shape[0] // BATCH_SIZE
            )
            # validation_data=(X_validation, [Y_valid_motion,Y_valid_phase]))
        model.save(model_file)
        plot_model(model, to_file=model_file.replace('.hdf5', '_structure.png'), show_shapes=True)

```

課題点
- 以下のエラーでる。TPUでデータが対応していないとのこと…
```
InvalidArgumentError: Unsupported data type for TPU: double, caused by output cond_8/Merge:0
```
- [この記事](https://lang-int.hatenablog.com/entry/2019/04/29/162132)の「バッチサイズ以外の次元が確実に数値で入るようにする」あたりが原因かなぁ

注意点
- 細かいけど、inputという変数はないらしく、TPUだとエラー吐く。kerasならいけるのに！
```python
# input=x だとエラー吐く
model = Model(x, outputs=[out1, out2])
```

### 実行してもTPUが使われてないことがある (スクリプトの中身等、一部情報が古い)

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
    - 同期してたらだいじょうぶなはずだが

## Colaboratory上からファイルをダウンロード

左のサブ画面の「ファイル」から保存したいファイルまでカーソルを近づけて右クリック。「ダウンロード」で保存できる。

フォルダのダウンロードは出来ない。