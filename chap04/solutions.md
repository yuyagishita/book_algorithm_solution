# 4.1 o
フィボナッチ数列の時と同じような感じで実装をする。

# 4.2 o
メモ化すると計算量がO(N)になる。
一度計算した値は保存しておくので、同じ計算をしないので。

# 4.3 △
N=0のときは、$F_0 = \frac{1}{\sqrt{5}}((\frac{1+\sqrt{5}}{2})^0 - (\frac{1-\sqrt{5}}{2})^0) = 0$  
N=1のときは、$F_1 = \frac{1}{\sqrt{5}}((\frac{1+\sqrt{5}}{2})^1 - (\frac{1-\sqrt{5}}{2})^1) = 1$  
N=2のときは、$F_2 = \frac{1}{\sqrt{5}}((\frac{1+\sqrt{5}}{2})^2 - (\frac{1-\sqrt{5}}{2})^2) = 1$  
N=3のときは、$F_3 = \frac{1}{\sqrt{5}}((\frac{1+\sqrt{5}}{2})^3 - (\frac{1-\sqrt{5}}{2})^3) = 2$  
フィボナッチ数列の実際の値と等しいのでこの数式は合っている。

## 解説見た
特性方程式で解ける。懐かしい。

# 4.4 △
4.3で証明された数式から考える。
O(N)記法だ定数倍とか定数項は無視できるので、$O(N) = ((\frac{1+\sqrt{5}}{2})^N$になる。

## 解説見た
$(\frac{1-\sqrt{5}}{2})^n$はnを無限に近づけると0になる。

# 4.5 x
全探索を再帰関数でといてほしんだろうな。この問題。
うまく解けなかったので回答を確認した。

## 解説見た
bitで記録させる方法がとても頭いい。再帰関数の使い方がそれぞれの3パターンで桁を増やしていく。
で与えられた数値よりも値が大きくなったらその地点をベースケースにする。
753が入っているのかのフラグにはbitを使う。もしn>kまでにbitで111にできなかったら答えが増えずに前の再起に戻るシステム。

# 4.6 o
メモ化するためにmemo[n][w]を用意した。残りN個でWを作らないといけないときに作れるかどうかを入れる。
