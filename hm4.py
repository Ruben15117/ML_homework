import numpy as np
import matplotlib.pyplot as plt

def getMode(data):
    vals, counts = np.unique(data, return_counts=True)
    return vals[np.argmax(counts)]

def show(data, name):
    mean = np.mean(data)
    median = np.median(data)
    mode = getMode(np.round(data, 2))

    plt.figure(figsize=(8, 4))
    plt.hist(data, bins=50, density=True, color='lightgray', alpha=0.6, edgecolor='black')

    plt.axvline(mean, color='blue', linestyle='--', linewidth=2, label=f'Mean = {mean:.2f}')
    plt.axvline(median, color='red', linestyle='-.', linewidth=2, label=f'Median = {median:.2f}')
    plt.axvline(mode, color='black', linestyle=':', linewidth=2, label=f'Mode = {mode:.2f}')

    plt.title(name)
    plt.legend()
    plt.show()

normal = np.random.normal(0, 1, 10000)
show(normal, "Normal")

bernoulli = np.random.binomial(1, 0.4, 10000)
show(bernoulli, "Bernoulli")

weibull = np.random.weibull(2.5, 10000)
show(weibull, "Weibull")

expon = np.random.exponential(2.0, 10000)
show(expon, "Exponential")