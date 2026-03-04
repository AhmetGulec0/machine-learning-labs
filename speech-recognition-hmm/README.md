# HMM ile İzole Kelime Tanıma Sistemi

### 1. Problem Tanımı
[cite_start]Bu projede **Hidden Markov Model (HMM)** kullanılarak basit bir konuşma tanıma sistemi simüle edilmiştir[cite: 2, 20]. [cite_start]Amaç, "EV" ve "OKUL" kelimelerini temsil eden iki ayrı HMM modeli oluşturmak ve gelen bir gözlem dizisinin hangi kelimeye daha yakın olduğunu **Log-Likelihood** değeri ile belirlemektir[cite: 23, 26].

### 2. Kullanılan Yöntem
[cite_start]Projede Python dili ve `hmmlearn` kütüphanesi kullanılmıştır[cite: 22, 28]. 
* [cite_start]**Durumlar (Hidden States)**: Kelimeyi oluşturan fonemleri temsil eder[cite: 4, 5].
* [cite_start]**Gözlemler (Observations)**: Sesin frekans karakteristiğini (High / Low) temsil eder[cite: 9].
* [cite_start]**Model Parametreleri**: Başlangıç ($\pi$), Geçiş ($A$) ve Emisyon ($B$) olasılık matrisleri tanımlanmıştır[cite: 10, 11, 14].

### 3. Klasör Yapısı
[cite_start]Hocanın belirttiği standartlara uygun olarak proje dizini şu şekildedir[cite: 44, 46, 49]:
* [cite_start]**`src/`**: `recognizer.py` (HMM sınıflandırıcı kodu) [cite: 48]
* [cite_start]**`report/`**: `cozum_anahtari.pdf` (Viterbi çözümü ve analiz soruları) [cite: 50]
* [cite_start]**`requirements.txt`**: Gerekli kütüphaneler (`hmmlearn`, `numpy`) [cite: 51]
* [cite_start]**`README.md`**: Proje açıklaması ve tartışma [cite: 52]

### 4. Çalıştırma Talimatları
1. Gerekli kütüphaneleri kurun:
   ```bash
   pip install -r requirements.txt
