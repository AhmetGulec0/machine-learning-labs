# HMM ile İzole Kelime Tanıma Sistemi

### 1. Problem Tanımı
Bu projede **Hidden Markov Model (HMM)** kullanılarak basit bir konuşma tanıma sistemi simüle edilmiştir. Amaç, "EV" ve "OKUL" kelimelerini temsil eden iki ayrı HMM modeli oluşturmak ve gelen bir gözlem dizisinin hangi kelimeye daha yakın olduğunu **Log-Likelihood** değeri ile belirlemektir.

### 2. Kullanılan Yöntem
Projede Python dili ve `hmmlearn` kütüphanesi kullanılmıştır. 
* **Durumlar (Hidden States)**: Kelimeyi oluşturan fonemleri temsil eder.
* **Gözlemler (Observations)**: Sesin frekans karakteristiğini (High / Low) temsil eder.
* **Model Parametreleri**: Başlangıç ($\pi$), Geçiş ($A$) ve Emisyon ($B$) olasılık matrisleri tanımlanmıştır.

### 3. Klasör Yapısı
Hocanın belirttiği standartlara uygun olarak proje dizini şu şekildedir:
* **`src/`**: `recognizer.py` (HMM sınıflandırıcı kodu)
* **`report/`**: `cozum_anahtari.pdf` (Viterbi çözümü ve analiz soruları)
* **`requirements.txt`**: Gerekli kütüphaneler (`hmmlearn`, `numpy`)
* **`README.md`**: Proje açıklaması ve tartışma

### 4. Çalıştırma Talimatları
1. Gerekli kütüphaneleri kurun:
   ```bash
   pip install -r requirements.txt
