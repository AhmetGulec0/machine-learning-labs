# 🌌 Uzak Bir Galaksinin Parlaklık Analizi (Bayesian Inference)

## 📌 1. Problem Tanımı

Bu projede, gürültülü gözlem verileri kullanılarak bir gök cisminin gerçek parlaklığı (**μ**) ve gözlem belirsizliği (**σ**) Bayesyen çıkarım yöntemi ile tahmin edilmiştir.

Amaç:

* Gerçek değere ne kadar yaklaşıldığını görmek
* Belirsizliği (uncertainty) modellemek
* MCMC (Markov Chain Monte Carlo) yöntemini uygulamak

---

## 📊 2. Kullanılan Veri

Veriler sentetik olarak oluşturulmuştur:

* Gerçek parlaklık (μ): **150.0**
* Gerçek hata (σ): **10.0**
* Gözlem sayısı: **50**

Veri üretimi:

```python
data = true_mu + true_sigma * np.random.randn(n_obs)
```

---

## ⚙️ 3. Kullanılan Yöntem

Bu projede Bayes Teoremi kullanılmıştır:

Posterior ∝ Likelihood × Prior

### Kullanılan bileşenler:

* **Likelihood:** Gaussian dağılım
* **Prior:** Uniform dağılım
  (0 < μ < 300, 0 < σ < 50)
* **Posterior:** log_prior + log_likelihood

### Kullanılan araçlar:

* `emcee` → MCMC örnekleme
* `corner` → Posterior görselleştirme
* `matplotlib` → Grafikler

---

## 🔁 4. MCMC (Markov Chain Monte Carlo)

* Walker sayısı: **32**
* Adım sayısı: **2000**
* Burn-in: **500**
* Thin: **15**

MCMC sayesinde parametrelerin olasılık dağılımları elde edilmiştir.

---

## 📈 5. Sonuçlar

| Parametre     | Gerçek Değer | Median                 | %16    | %84    | Mutlak Hata |
| ------------- | ------------ | ---------------------- | ------ | ------ | ----------- |
| μ (Parlaklık) | 150.0        | (results.txt'ten ekle) | (ekle) | (ekle) | (ekle)      |
| σ (Hata)      | 10.0         | (results.txt'ten ekle) | (ekle) | (ekle) | (ekle)      |

📌 Not: Bu değerleri `report/results.txt` dosyasından kopyalayınız.

---

## 📉 6. Grafikler

### 🔹 Corner Plot

* Parametre dağılımlarını gösterir
* μ ve σ arasındaki ilişkiyi analiz eder

### 🔹 Trace Plot

* MCMC zincirlerinin stabil olup olmadığını gösterir

Grafikler `report/` klasöründe bulunmaktadır.

---

## 🧠 7. Analiz ve Yorum

### ✔ Doğruluk (Accuracy)

Model, gerçek μ = 150 değerine oldukça yakın sonuç üretmiştir.
Bu da Bayesyen yöntemin yüksek doğrulukta çalıştığını gösterir.

---

### ✔ Hassasiyet (Precision)

μ parametresi σ’ya göre daha hassas tahmin edilmiştir.

Sebep:

* Ortalama doğrudan veri merkezine bağlıdır
* Sigma dağılımı temsil eder → daha belirsizdir

---

### ✔ Prior Etkisi

Dar bir prior seçilirse:

* Posterior yanlış yöne kayabilir
* Model bias üretir

---

### ✔ Veri Miktarı Etkisi

* n azalırsa → belirsizlik artar
* n artarsa → posterior daralır

---

### ✔ Korelasyon Analizi

Corner plot’ta:

* Eğik elips → korelasyon
* Dikey dağılım → bağımsızlık

Bu projede μ ve σ arasında hafif korelasyon gözlemlenebilir.

---

## 📂 8. Klasör Yapısı

```
4-bayesian-brightness-analysis/
├── src/
│   └── brightness_analysis.py
├── report/
│   ├── corner_plot.png
│   ├── trace_plot.png
│   ├── results.txt
│   └── yorumlar_ve_grafikler.pdf
├── README.md
└── requirements.txt
```

---

## ▶️ 9. Çalıştırma

```bash
pip install -r requirements.txt
python src/brightness_analysis.py
```

---

## 📌 10. Notlar

* Her çalıştırmada sonuçlar biraz değişebilir (rastgelelik nedeniyle)
* Bu durum Bayesyen yöntemlerin doğası gereğidir

---

## ✨ Sonuç

Bu projede Bayesyen çıkarım kullanılarak:

* Parametre tahmini yapılmış
* Belirsizlik modellenmiş
* MCMC yöntemi uygulanmıştır

Bu yaklaşım özellikle astronomi gibi gürültülü veri içeren alanlarda oldukça güçlüdür.
