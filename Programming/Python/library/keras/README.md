# テクニカル
1. SequentialとFunctionalAPI

Sequentialは今の層のそれぞれのノードに、前の層の全ノードから矢印を引っ張ってくるイメージ。「A→B→C」の流れ。
FunctionalAPIでは 2つのニューラルネットワークの出力を入れてみたり、レイヤーを共有してみたりと、結構複雑なことができる。「A→B1(→B2)→C」という風にB1とB2に枝分かれさせることが可能。

参考記事：https://qiita.com/Ishotihadus/items/e28dd461a8ba27a2676e