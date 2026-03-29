# Ödev 3: Özdeğerler ve Özvektörler Teknik Raporu

## 1. Makine Öğrenmesi ve Lineer Cebir İlişkisi

Makine öğrenmesi modelleri, yüksek boyutlu verileri matrisler aracılığıyla temsil eder. Veri setleri üzerindeki dönüşümler, boyut indirgeme ve özellik çıkarımı gibi işlemler doğrudan lineer cebir prensiplerine dayanmaktadır.

### 1.1. Özdeğer (Eigenvalue) ve Özvektör (Eigenvector) Kavramları
Bir kare matris $A$ ile bir $v$ vektörü çarpıldığında, eğer sonuç vektörü başlangıçtaki $v$ vektörünün doğrultusunu değiştirmiyor, sadece boyutu bir skaler ($\lambda$) katı kadar ölçekleniyorsa; $v$ vektörüne **özvektör**, $\lambda$ değerine ise bu vektöre karşılık gelen **özdeğer** denir:
$$Av = \lambda v$$



### 1.2. Makine Öğrenmesindeki Kritik Uygulamalar
* **Temel Bileşen Analizi (PCA):** Verinin kovaryans matrisinin özdeğerleri ve özvektörleri hesaplanarak, verideki en yüksek varyansı temsil eden "ana bileşenler" bulunur. Bu, bilgi kaybını minimize ederek boyut küçültmeyi sağlar.
* **Spektral Kümeleme (Spectral Clustering):** Karmaşık veri yapılarında, benzerlik matrisinin özdeğer spektrumu kullanılarak veri noktaları gruplandırılır.
* **Google PageRank:** Web sayfalarının önem sırasını belirleyen algoritma, devasa bir bağlantı matrisinin en baskın özvektörünün (eigenvector centrality) hesaplanmasına dayanır.

---

## 2. Numpy `linalg.eig` Fonksiyonu Teknik Analizi

Numpy kütüphanesi, lineer cebir işlemlerinde endüstri standardı olan düşük seviyeli kütüphaneleri kullanır.

### 2.1. Fonksiyon Dokümantasyonu
`numpy.linalg.eig(a)` fonksiyonu, girdi olarak aldığı kare matrisin sağ özvektörlerini ve bunlara karşılık gelen özdeğerlerini iki ayrı yapı olarak döndürür. Özvektörler, sütunlar halinde normalize edilmiş bir matris olarak sunulur.

### 2.2. Algoritmik Arka Plan (Kaynak Kod Analizi)
Numpy'ın `linalg.py` kaynak kodları incelendiğinde, işlemin doğrudan Python seviyesinde değil, **LAPACK (Linear Algebra Package)** kütüphanesine yapılan çağrılarla yürütüldüğü görülür.
* **Rutin:** Genel (simetrik olmayan) gerçek matrisler için `dgeev` rutini kullanılır.
* **Yöntem:** Matris önce üst üçgensel (Hessenberg) forma indirgenir. Ardından iteratif bir yöntem olan **QR Algoritması** kullanılarak özdeğerler yakınsama yoluyla hesaplanır.



---

## 3. Manuel ve Hesaplamalı Analiz Karşılaştırması

Bu çalışmada, 2x2 boyutundaki bir örnek matrisin özdeğerleri hem karakteristik denklem ($det(A - \lambda I) = 0$) kullanılarak manuel olarak çözülmüş, hem de Numpy sonuçlarıyla karşılaştırılmıştır. Detaylı analiz çıktıları `src/` klasöründeki Notebook dosyasında mevcuttur.

---

## 4. Kaynakça

1. **Brownlee, J. (2018).** *Introduction to Matrices and Matrix Arithmetic for Machine Learning*. Machine Learning Mastery.
2. **Numpy Documentation.** *Linear Algebra (numpy.linalg.eig)*. [Erişim: numpy.org]
3. **Strang, G. (2016).** *Introduction to Linear Algebra*. Wellesley-Cambridge Press.
4. **Numpy GitHub Repository.** *Source code for linalg.py*. [Erişim: github.com/numpy]
5. **Machine Learning Mastery.** *Gentle Introduction to Eigenvalues and Eigenvectors for Machine Learning*.
