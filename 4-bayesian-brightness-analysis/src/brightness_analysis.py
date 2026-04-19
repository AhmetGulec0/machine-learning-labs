import os
import numpy as np
import matplotlib.pyplot as plt
import emcee
import corner


# =========================================================
# 1) KLASOR HAZIRLIGI
# =========================================================
OUTPUT_DIR = "report"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# =========================================================
# 2) SENTETIK VERI URETIMI
# =========================================================
np.random.seed(42)

true_mu = 150.0       # Gercek parlaklik
true_sigma = 10.0     # Gercek olcum hatasi
n_obs = 50            # Gozlem sayisi

data = true_mu + true_sigma * np.random.randn(n_obs)


# =========================================================
# 3) BAYESYEN FONKSIYONLAR
# =========================================================
def log_likelihood(theta, data):
    """
    Gaussian likelihood:
    theta = (mu, sigma)
    """
    mu, sigma = theta

    if sigma <= 0:
        return -np.inf

    return -0.5 * np.sum(((data - mu) / sigma) ** 2 + np.log(2 * np.pi * sigma ** 2))


def log_prior(theta):
    """
    Uniform prior:
    0 < mu < 300
    0 < sigma < 50
    """
    mu, sigma = theta

    if 0 < mu < 300 and 0 < sigma < 50:
        return 0.0

    return -np.inf


def log_probability(theta, data):
    """
    log posterior = log prior + log likelihood
    """
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, data)


# =========================================================
# 4) MCMC AYARLARI
# =========================================================
initial = np.array([140.0, 5.0])
n_walkers = 32
n_dim = 2
n_steps = 2000
burn_in = 500
thin_step = 15

# Baslangic noktalarini initial etrafinda biraz dagitiyoruz
pos = initial + 1e-4 * np.random.randn(n_walkers, n_dim)

sampler = emcee.EnsembleSampler(n_walkers, n_dim, log_probability, args=(data,))
sampler.run_mcmc(pos, n_steps, progress=True)


# =========================================================
# 5) ORNEKLERI TOPLAMA
# =========================================================
flat_samples = sampler.get_chain(discard=burn_in, thin=thin_step, flat=True)

mu_samples = flat_samples[:, 0]
sigma_samples = flat_samples[:, 1]


# =========================================================
# 6) OZET ISTATISTIKLER
# =========================================================
mu_q16, mu_median, mu_q84 = np.percentile(mu_samples, [16, 50, 84])
sigma_q16, sigma_median, sigma_q84 = np.percentile(sigma_samples, [16, 50, 84])

mu_abs_error = abs(mu_median - true_mu)
sigma_abs_error = abs(sigma_median - true_sigma)

mu_percent_error = (mu_abs_error / true_mu) * 100
sigma_percent_error = (sigma_abs_error / true_sigma) * 100


# =========================================================
# 7) SONUCLARI TERMINALE YAZDIRMA
# =========================================================
print("\n" + "=" * 60)
print("GERCEK DEGERLER")
print("=" * 60)
print(f"true_mu    = {true_mu}")
print(f"true_sigma = {true_sigma}")
print(f"n_obs      = {n_obs}")

print("\n" + "=" * 60)
print("POSTERIOR OZETLERI")
print("=" * 60)
print(
    f"mu (Parlaklik): median = {mu_median:.4f}, "
    f"%16 = {mu_q16:.4f}, %84 = {mu_q84:.4f}, "
    f"mutlak hata = {mu_abs_error:.4f}, yuzde hata = {mu_percent_error:.2f}%"
)
print(
    f"sigma (Hata):  median = {sigma_median:.4f}, "
    f"%16 = {sigma_q16:.4f}, %84 = {sigma_q84:.4f}, "
    f"mutlak hata = {sigma_abs_error:.4f}, yuzde hata = {sigma_percent_error:.2f}%"
)

mu_ci_95 = np.percentile(mu_samples, [2.5, 97.5])
sigma_ci_95 = np.percentile(sigma_samples, [2.5, 97.5])

print("\n%95 Guven Araliklari")
print(f"mu    : [{mu_ci_95[0]:.4f}, {mu_ci_95[1]:.4f}]")
print(f"sigma : [{sigma_ci_95[0]:.4f}, {sigma_ci_95[1]:.4f}]")


# =========================================================
# 8) SONUCLARI DOSYAYA YAZMA
# =========================================================
results_path = os.path.join(OUTPUT_DIR, "results.txt")
with open(results_path, "w", encoding="utf-8") as f:
    f.write("YZM212 Makine Ogrenmesi 4. Odev Sonuclari\n")
    f.write("=" * 60 + "\n\n")

    f.write("Gercek Degerler\n")
    f.write(f"true_mu    = {true_mu}\n")
    f.write(f"true_sigma = {true_sigma}\n")
    f.write(f"n_obs      = {n_obs}\n\n")

    f.write("Posterior Ozetleri\n")
    f.write(
        f"mu (Parlaklik): median = {mu_median:.4f}, "
        f"%16 = {mu_q16:.4f}, %84 = {mu_q84:.4f}, "
        f"mutlak hata = {mu_abs_error:.4f}, yuzde hata = {mu_percent_error:.2f}%\n"
    )
    f.write(
        f"sigma (Hata): median = {sigma_median:.4f}, "
        f"%16 = {sigma_q16:.4f}, %84 = {sigma_q84:.4f}, "
        f"mutlak hata = {sigma_abs_error:.4f}, yuzde hata = {sigma_percent_error:.2f}%\n\n"
    )

    f.write("%95 Guven Araliklari\n")
    f.write(f"mu    : [{mu_ci_95[0]:.4f}, {mu_ci_95[1]:.4f}]\n")
    f.write(f"sigma : [{sigma_ci_95[0]:.4f}, {sigma_ci_95[1]:.4f}]\n\n")

    f.write("Tablo Icin Ozet\n")
    f.write(
        f"mu,{true_mu:.4f},{mu_median:.4f},{mu_q16:.4f},{mu_q84:.4f},{mu_abs_error:.4f}\n"
    )
    f.write(
        f"sigma,{true_sigma:.4f},{sigma_median:.4f},{sigma_q16:.4f},{sigma_q84:.4f},{sigma_abs_error:.4f}\n"
    )


# =========================================================
# 9) TRACE PLOT
# =========================================================
chains = sampler.get_chain()

fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

axes[0].plot(chains[:, :, 0], alpha=0.35)
axes[0].axhline(true_mu, linestyle="--")
axes[0].set_ylabel("mu")
axes[0].set_title("Trace Plot - mu")

axes[1].plot(chains[:, :, 1], alpha=0.35)
axes[1].axhline(true_sigma, linestyle="--")
axes[1].set_ylabel("sigma")
axes[1].set_xlabel("Adim")
axes[1].set_title("Trace Plot - sigma")

plt.tight_layout()
trace_plot_path = os.path.join(OUTPUT_DIR, "trace_plot.png")
plt.savefig(trace_plot_path, dpi=300, bbox_inches="tight")
plt.close()


# =========================================================
# 10) CORNER PLOT
# =========================================================
fig = corner.corner(
    flat_samples,
    labels=[r"$\mu$ (Parlaklik)", r"$\sigma$ (Hata)"],
    truths=[true_mu, true_sigma],
    show_titles=True,
    title_fmt=".3f"
)

corner_plot_path = os.path.join(OUTPUT_DIR, "corner_plot.png")
plt.savefig(corner_plot_path, dpi=300, bbox_inches="tight")
plt.close()


# =========================================================
# 11) VERI HISTOGRAMI
# =========================================================
plt.figure(figsize=(8, 5))
plt.hist(data, bins=12, density=True, alpha=0.7)
plt.axvline(true_mu, linestyle="--", label=f"Gercek mu = {true_mu}")
plt.axvline(mu_median, linestyle=":", label=f"Tahmin edilen mu = {mu_median:.2f}")
plt.xlabel("Parlaklik Gozlemi")
plt.ylabel("Yogunluk")
plt.title("Sentetik Gozlem Verisinin Dagilimi")
plt.legend()
hist_path = os.path.join(OUTPUT_DIR, "data_histogram.png")
plt.tight_layout()
plt.savefig(hist_path, dpi=300, bbox_inches="tight")
plt.close()


# =========================================================
# 12) KISA YORUM DOSYASI
# =========================================================
comment_path = os.path.join(OUTPUT_DIR, "short_interpretation.txt")
with open(comment_path, "w", encoding="utf-8") as f:
    f.write("Kisa Yorumlar\n")
    f.write("=" * 50 + "\n\n")

    f.write("1) Dogruluk Analizi\n")
    f.write(
        f"Model, gercek mu = {true_mu} degerine karsi posterior median olarak "
        f"{mu_median:.4f} bulmustur. Mutlak hata {mu_abs_error:.4f} oldugu icin "
        "tahminin gercek degere oldukca yakin oldugu soylenebilir.\n\n"
    )

    f.write("2) Hassasiyet Karsilastirmasi\n")
    f.write(
        "Genellikle mu parametresinin tahmini sigma parametresine gore daha hassastir. "
        "Bunun nedeni ortalamanin verideki merkezi egilimi dogrudan temsil etmesi, "
        "sigma'nin ise yayilimi tahmin etmesi ve daha fazla belirsizlik icermesidir.\n\n"
    )

    f.write("3) Prior Etkisi\n")
    f.write(
        "Eger mu icin cok dar ve yanlis bir prior secilirse posterior dagilim veri ile "
        "prior arasinda bir uzlasma kurar ve sonuc gercek degere gore kayabilir.\n\n"
    )

    f.write("4) Veri Miktari Etkisi\n")
    f.write(
        "Gozlem sayisi azaltilirsa posterior dagilim genisler, yani belirsizlik artar. "
        "Daha cok veri daha dar bir posterior verir.\n\n"
    )

    f.write("5) Corner Plot Yorumu\n")
    f.write(
        "Corner plot uzerindeki ortak dagilim egikse parametreler arasinda korelasyon "
        "olabilir; dik ve daha simetrikse bagimsizlik daha gucludur.\n"
    )


print("\nDosyalar olusturuldu:")
print(f"- {results_path}")
print(f"- {trace_plot_path}")
print(f"- {corner_plot_path}")
print(f"- {hist_path}")
print(f"- {comment_path}")
print("\nAnaliz tamamlandi.")
