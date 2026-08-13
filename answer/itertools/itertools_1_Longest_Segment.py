import math
from itertools import combinations
# import numpy as np  (※AtCoderではNumpyも使えますが、今回はmathで代用する例も示します)

# 【方針】
# 存在する全ての2点の組み合わせを試し、距離の最大値を求めます。
# ルート（√）の計算は処理が重いため、ループ内では「距離の2乗」のまま最大値を更新し続け、
# 最後に1回だけルートを計算して出力するのが高速化のコツです。

N = int(input())

# 1. 入力の受け取り（リスト内包表記を使うとスッキリ書けます）
xy_L = [list(map(int, input().split())) for _ in range(N)]

max_dist_sq = 0  # 距離の「2乗」の最大値を保持する変数

# 2. combinations を使って全探索
# 二重ループ（for i... for j...）を書かなくても、2点を選ぶ全パターンを自動で列挙してくれます
for xy_1, xy_2 in combinations(xy_L, 2):
    
    # 2点間の距離の2乗を計算: (x1 - x2)^2 + (y1 - y2)^2
    dist_sq = (xy_1[0] - xy_2[0])**2 + (xy_1[1] - xy_2[1])**2
    
    # 最大値を更新
    max_dist_sq = max(max_dist_sq, dist_sq)

# 3. 最後に1回だけルートを計算して出力
# math.sqrt(max_dist_sq) や max_dist_sq**0.5 を使うのが競技プログラミングの主流です。
# （もちろん np.sqrt を使っても問題ありません！）
print(math.sqrt(max_dist_sq))