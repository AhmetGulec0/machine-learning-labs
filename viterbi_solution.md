# Viterbi Algoritması Çözümü

Durumlar: S = {e, v}

Gözlemler: O = {High, Low}

Başlangıç: P(e) = 1.0

Geçiş Olasılıkları

e→e = 0.6\
e→v = 0.4\
v→v = 0.8\
v→e = 0.2

Emisyon Olasılıkları

e: High = 0.7 Low = 0.3

v: High = 0.1 Low = 0.9

Gözlem dizisi: \[High, Low\]

Adım 1

δ1(e) = 1.0 × 0.7 = 0.7

Adım 2

e→e: 0.7 × 0.6 × 0.3 = 0.126

v→e: 0

δ2(e) = 0.126

e→v: 0.7 × 0.4 × 0.9 = 0.252

v→v: 0

δ2(v) = 0.252

Sonuç:

En büyük değer 0.252 olduğu için en olası durum dizisi:

\[e, v\]
