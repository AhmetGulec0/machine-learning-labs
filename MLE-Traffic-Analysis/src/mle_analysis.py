# ==========================================================
# BAĞIMLILIKLAR (Kütüphanelerin Import Edilmesi)
# ==========================================================
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from scipy.stats import poisson

# ==========================================================
# BÖLÜM 2: VERİ TANIMLAMA VE HAZIRLIK
# ==========================================================
# Dakika başına geçen araç sayılarını temsil eden örnek veri seti
# Bu veriler Poisson analizi için temel teşkil eder.
traffic_data = np.array([12, 15, 10, 18, 14, 16, 11, 13, 15, 14])

# ==========================================================
# BÖLÜM 3: MLE FONKSİYONU VE OPTİMİZASYON
# ==========================================================

def calculate_negative_log_likelihood(mu, observations):
    """
    Poisson dağılımı için Negatif Log-Likelihood değerini hesaplar.
    Minimize edilerek en uygun Lambda (mu) değeri bulunur.
    """
    if mu <= 0:
        return 1e10 # Geçersiz lambda değerlerini engellemek için büyük bir ceza değeri
    
    n = len(observations)
    # Log-Likelihood Formülü: -n*mu + sum(xi)*ln(mu)
    log_likelihood = -n * mu + np.sum(observations) * np.log(mu)
    
    # Minimize fonksiyonu için negatif değer döndürülür
    return -log_likelihood

# Başlangıç tahmini (Initial guess)
initial_mu = traffic_data.mean() 

# Scipy minimize kullanarak en iyi Lambda değerinin bulunması
optimization_result = minimize(
    calculate_negative_log_likelihood, 
    initial_mu, 
    args=(traffic_data,), 
    method='L-BFGS-B', 
    bounds=[(0.001, None)]
)

mle_lambda = optimization_result.x[0]

# Sonuçların raporlanması
print(f"Sayısal Optimizasyon ile Bulunan Lambda: {mle_lambda:.4f}")
print(f"Teorik Beklenti (Veri Ortalaması): {traffic_data.mean():.4f}")

# ==========================================================
# BÖLÜM 4: GÖRSELLEŞTİRME
# ==========================================================

plt.figure(figsize=(10, 6))

# Gerçek verinin dağılımı (Histogram)
plt.hist(traffic_data, bins=range(min(traffic_data), max(traffic_data) + 2), 
         density=True, alpha=0.6, color='skyblue', edgecolor='black', 
         label='Gözlemlenen Araç Sayıları', align='left')

# MLE ile tahmin edilen parametreye göre Poisson PMF eğrisi
x_range = np.arange(min(traffic_data)-2, max(traffic_data)+3)
plt.plot(x_range, poisson.pmf(x_range, mle_lambda), 'ro--', 
         linewidth=2, markersize=6, label=f'Poisson Modeli (λ={mle_lambda:.2f})')

# Zorunlu Grafik Bileşenleri
plt.title('Trafik Yoğunluğu Analizi: Gerçek Veri vs Poisson Modeli') # Başlık
plt.xlabel('Dakika Başına Araç Sayısı (k)') # X Ekseni
plt.ylabel('Gözlemlenme Olasılığı / Frekans') # Y Ekseni
plt.legend() # Gösterge
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
