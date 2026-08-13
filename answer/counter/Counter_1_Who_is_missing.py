from collections import Counter

N = int(input())
A = list(map(int, input().split()))
c = Counter(A)  # クラスのインスタンスを作成
print(c.most_common()[-1][0])  # most_commonによって頻度順で並べ、得られたタプルのただ一つのkeyをprintして答え

# print(c)  # dict型を継承して作られているため、dictの様になっていることが確認できる(printで出力できるように作られている)。