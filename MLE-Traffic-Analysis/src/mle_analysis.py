import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from scipy.stats import poisson

raw_data = np.array([14, 12, 16, 13, 15, 12, 14, 17, 13, 15])

def log_likelihood_function(mu, x):
    if mu <= 0:
        return 1e10
    n = len(x)
    val = -n * mu + np.sum(x) * np.log(mu)
    return -val

init_mu = 1.0
opt_result = minimize(log_likelihood_function, init_mu, args=(raw_data,), method='L-BFGS-B', bounds=[(0.001, None)])
final_lambda = opt_result.x[0]

print(f"Result (Lambda): {final_lambda}")
print(f"Mean: {np.mean(raw_data)}")

plt.figure()
plt.hist(raw_data, bins=range(min(raw_data), max(raw_data) + 2), density=True, alpha=0.7, color='gray', align='left')
x_axis = np.arange(min(raw_data)-2, max(raw_data)+3)
plt.plot(x_axis, poisson.pmf(x_axis, final_lambda), 'k-o')
plt.show()

def check_outlier(d, val):
    updated_data = np.append(d, val)
    return np.mean(updated_data)

print(f"Outlier Effect: {check_outlier(raw_data, 200)}")
