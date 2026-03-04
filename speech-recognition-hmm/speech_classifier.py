
import numpy as np
from hmmlearn import hmm

model_ev = hmm.MultinomialHMM(n_components=2)

model_ev.startprob_ = np.array([1.0, 0.0])

model_ev.transmat_ = np.array([
    [0.6, 0.4],
    [0.2, 0.8]
])

model_ev.emissionprob_ = np.array([
    [0.7, 0.3],
    [0.1, 0.9]
])

model_okul = hmm.MultinomialHMM(n_components=2)

model_okul.startprob_ = np.array([1.0, 0.0])

model_okul.transmat_ = np.array([
    [0.5, 0.5],
    [0.3, 0.7]
])

model_okul.emissionprob_ = np.array([
    [0.6, 0.4],
    [0.2, 0.8]
])

# High = 0
# Low = 1
test = np.array([[0], [1]])

score_ev = model_ev.score(test)
score_okul = model_okul.score(test)

if score_ev > score_okul:
    print("Tahmin edilen kelime: EV")
else:
    print("Tahmin edilen kelime: OKUL")

print("EV log likelihood:", score_ev)
print("OKUL log likelihood:", score_okul)
