# 9.1 x

そもそも連結リストを Python でどうやって実装するのかが見えてなかった。
連結リストに関する学習にほとんど時間を費やした。

## 解説見た

解説見るまでは pop するのは末尾の連結リストだと思い込んでいたがデータ構造的に先頭を削除するのが一番楽。
で先頭にも末尾にも連結リストを追加するのは簡単なので削除の扱いを工夫できれば問題なかった。

# 9.2 o

スタックを用いる。数字を見つけたらスタックに入れていく。
演算子が見つかったらスタックから 2 つ取り出して計算をする。結果をスタックに入れる。
これを繰り返す。  
collections の deque を使ってもいいがせっかくなので自分で実装をする。
というよりも、普通に配列を使えば解けそう。

# 9.3 o

スタックを用いる。
