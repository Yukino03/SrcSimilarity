# ソースコードの類似度判定

## 目的

プログラムの類似度を判定する目的を明らかにする必要がある。
岩村らは

プログラムの類似度を判定するという行為には複数の解釈が考えられる。

1. 機能的な類似度
入力に対する出力内容が同一ならば類似していると考えられる。
この調査にはブラックボックステストが適していると考えられる。

1. 内部処理的類似度
プログラムが内部的にどのような処理をしているかを比較する。
コード内容を比較する必要がある。
この場合、一つの処理を複数の命令に分割する場合や、異なる変数名を使う場合も同一処理として
考える必要がある。

## 実験環境

- Python3.6.5

## 実験方法

- Pythonを使用

## 問題点

- プログラムコードが極端に短い場合。
- 言語が異なる場合(比較手法に工夫が必要)
  - 第３の言語に変換してからの比較?

## 仕様書

```python
import sys

class SrcFile():
  def __init__(self, filepath):
    self.__path = filepath
    self.read_file(filepath)

  def read_file(self, filepath):
    with open(filepath) as f:
      self.__lines = [s.rstrip() for s in f.readlines()]

  def print_src(self):
    for line in self.__lines:
      print(line)

  def get_line(self, n):
    return self.__lines[n]

  def get_path(self):
    return self.__path

  def get_len(self):
    return len(self.__lines)

if __name__ == "__main__":
  args = sys.argv
  if len(args) != 2:
    print("Argument Error")
    sys.exit(1)
  else:
    src = SrcFile(args[1])
    src.print_src()
    print(src.get_line(0))
    sys.exit(0)
```
