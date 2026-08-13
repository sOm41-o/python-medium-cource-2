from itertools import combinations

# 【方針】
# 3本の棒の選び方をすべて列挙し、それぞれが以下の2つの条件を満たすか判定します。
# 1. 3本の長さがすべて異なる
# 2. 3本で三角形を作ることができる (短い2辺の和 > 最も長い辺)

N = int(input())
L = list(map(int, input().split()))

count = 0

# 1. combinations を使って、N本の棒から3本を選ぶ全パターンを試す
for a, b, c in combinations(L, 3):
    
    # 3辺を短い順に並べ替える（常に c が一番長い辺になるようにする）
    a, b, c = sorted([a, b, c])
    
    # 2. 条件判定
    # len({a, b, c}) == 3 : 集合(set)にして要素数が3なら、すべて異なる長さ
    # a + b > c : 一番長い辺(c)より、残り2辺(a, b)の和が大きければ三角形になる
    if len({a, b, c}) == 3 and (a + b > c):
        count += 1

print(count)