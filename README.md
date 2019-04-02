# SrcSimilarity

## 目的

プログラムの類似度を判定するという行為には複数の解釈が考えられる。

1. 機能的な類似度
入力に対する出力内容の類似度。
この調査にはブラックボックステストが適していると考えられる。
実際に実行し、出力の比較を行う。

1. 内部処理的類似度
プログラムが内部処理の記述を比較する。
ソースコード自体を比較する必要がある。
この場合、一つの処理を複数の命令に分割する場合や、異なる変数名を使う場合も同一処理として
考える必要がある。

1. 出現単語の類似度
コード中の単語の出現頻度を

1. プログラム作成者の類似度
前者2つとは違い、作成者の特定という目的がある。
作成者のコードスタイルやプログラムの癖から一致度を算出する。

## 実験環境

- Python3.6.5

## 実験方法

- Pythonを使用

## 予想される問題点

- プログラムコードが極端に短い場合。
  - 特徴を十分に集められない。
- 言語が異なる場合(比較手法に工夫が必要)
  - 第３の言語に変換してからの比較?
- ジャロ・ウィンクラー距離
