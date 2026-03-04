# Analiz Soruları

## 1) Gürültü HMM modelini nasıl etkiler?

Ses verisindeki gürültü gözlem özelliklerinin doğru temsil edilmesini
zorlaştırır. HMM modelinde gözlemler emisyon olasılıkları ile temsil
edilir. Gürültü bulunduğunda gözlenen özellikler gerçek fonemi doğru
yansıtmayabilir.

Bu durum yanlış emisyon olasılıklarının oluşmasına neden olabilir ve
modelin yanlış fonem dizisini seçmesine yol açabilir.

## 2) Neden günümüzde Deep Learning tercih ediliyor?

Gerçek konuşma tanıma sistemlerinde binlerce kelime ve çok büyük veri
kümeleri bulunmaktadır.

HMM modelleri sınırlı yapıları nedeniyle karmaşık ses ilişkilerini
modellemede yetersiz kalabilir.

Deep Learning yöntemleri (RNN, LSTM, Transformer) zaman bağımlılıklarını
ve karmaşık özellikleri daha iyi öğrenebilir. Bu nedenle modern konuşma
tanıma sistemlerinde sıklıkla tercih edilmektedir.
