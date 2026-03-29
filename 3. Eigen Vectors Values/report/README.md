# Ödev 3: Özdeğerler ve Özvektörler Raporu

## 1. Makine Öğrenmesi ile İlişkisi
Makine öğrenmesinde özdeğerler, verinin "iskeletini" anlamamızı sağlar. Özellikle **PCA (Temel Bileşen Analizi)** gibi yöntemlerde, yüksek boyutlu veriyi en az bilgi kaybıyla düşük boyuta indirmek için kovaryans matrisinin özdeğerleri ve özvektörleri kullanılır.

*Referans:* [Machine Learning Mastery](https://machinelearningmastery.com/gentle-introduction-to-eigenvalues-and-eigenvectors-for-machine-learning/)

## 2. Numpy linalg.eig Analizi
Numpy'ın `eig` fonksiyonu, arka planda **LAPACK** kütüphanesini kullanarak matrisleri iteratif yöntemlerle (QR algoritması vb.) çözer. Bu sayede manuel hesaplamanın çok zor olduğu büyük matrislerde bile hızlı sonuç verir.
