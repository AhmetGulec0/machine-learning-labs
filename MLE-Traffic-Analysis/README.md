# MLE ile Akıllı Şehir Trafik Planlaması

### 1. Problem Tanımı
Bu projede, bir ana caddeden geçen dakikalık araç sayısını Poisson Dağılımı kullanarak modellemeyi amaçlıyoruz. En uygun yoğunluk parametresini (λ) bulmak için Maximum Likelihood Estimation (MLE) yöntemi kullanılmıştır.

### 2. Kullanılan Yöntem
* **Veri:** Bir dakikada geçen araç sayılarını içeren zaman serisi verisi.
* **Model:** Poisson Dağılımı $P(k|\lambda) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}$.
* **Tahmin:** Log-Likelihood fonksiyonunun türetilmesi ve Python ile sayısal optimizasyon (Scipy) yöntemleri.

### 3. Klasör Yapısı
* **src/**: MLE hesaplamalarını ve görselleştirmeleri içeren Python kodu.
* **report/**: Teorik türetmeleri ve "Outlier" analizini içeren PDF raporu.
* **requirements.txt**: Gerekli kütüphaneler (numpy, scipy, matplotlib).

### 4. Çalıştırma
Gerekli paketleri kurun:
`pip install -r requirements.txt`
Analizi başlatın:
`python src/mle_analysis.py`
