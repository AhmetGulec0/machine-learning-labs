# HMM ile İzole Kelime Tanıma Sistemi

## Problem Tanımı

Bu projede Hidden Markov Model (HMM) kullanılarak basit bir konuşma
tanıma sistemi simüle edilmiştir. Amaç iki farklı kelimeyi ("EV" ve
"OKUL") temsil eden iki ayrı HMM modeli oluşturmak ve gelen bir gözlem
dizisinin hangi kelimeye daha yakın olduğunu log-likelihood değeri ile
belirlemektir.

## Kullanılan Yöntem

Projede Python ve hmmlearn kütüphanesi kullanılmıştır. Her kelime için
ayrı bir HMM modeli oluşturulmuştur.

Durumlar: - Fonemleri temsil eder

Gözlemler: - Ses spektrumu özelliklerini temsil eder (High / Low)

Model parametreleri: - Başlangıç olasılıkları - Geçiş olasılıkları -
Emisyon olasılıkları

## Çalıştırma

Önce kütüphaneyi kurun:

pip install hmmlearn

Daha sonra:

python speech_classifier.py

## Dosyalar

speech_classifier.py -\> HMM kelime sınıflandırıcı kodu\
viterbi_solution.md -\> Teorik Viterbi çözümü\
analysis.md -\> Analiz sorularının cevapları

## Sonuç

Test gözlem dizisi için her iki modelin log-likelihood değeri
hesaplanır. Daha yüksek değeri veren model tahmin edilen kelime olarak
seçilir.
