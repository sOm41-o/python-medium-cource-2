import sys  # sys.exit()で強制終了させるために

from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

c_a = Counter(A)
c_b = Counter(B)

# あえてCounterで解くなら、こんな感じ
for key_b, value_b in c_b.items():
    if c_a[key_b] < value_b:
        print("No")
        sys.exit()
else:
    # for-else文というpythonicな文法。処理が途中で終了しなかった場合に、else文に移行する。
    print("Yes")

# 【学習ポイント】
# 1. c_a[key_b] について
# もしAの中にその長さの麺が1本もなかった場合、通常の辞書ならエラー(KeyError)になりますが、
# Counterは自動的に 0 を返してくれます。そのため条件分岐がこれ1つで済みます。

# 2. for-else文 について
# forループが「一度も break や sys.exit() で中断されずに最後まで回りきった場合」だけ
# elseの中の処理が実行されます。フラグ変数を使わなくて済む便利な構文です。