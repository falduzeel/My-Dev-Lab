import numpy as np

def fay_herriot(y, sampling_variances):
    m = len(y)
    y_bar = np.mean(y)
    sample_var = np.sum((y - y_bar) ** 2) / (m - 1)
    
    psi = max(0, sample_var - np.mean(sampling_variances))
    
    gamma = psi / (psi + sampling_variances)
    eblup = gamma * y + (1 - gamma) * y_bar
    return eblup, psi

y_observed = np.array([12.5, 14.1, 9.8, 11.2, 15.0])
variances = np.array([1.2, 0.8, 2.1, 1.5, 0.9])

eblup, psi = fay_herriot(y_observed, variances)
print("EBLUP Estimates:", eblup)
