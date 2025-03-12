import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

if __name__ == "__main__":
    lambda_ = np.linspace(0, 30, 1000)
    
    y = np.array([1, 7, 4, 8, 11, 12])
    N = y.size
    
    a0, b0 = 1, 1/10
    a, b = a0 + np.sum(y), b0 + N
    
    prior_pdf = gamma.pdf(lambda_, a0, scale=1/b0)
    posterior_pdf = gamma.pdf(lambda_, a, scale=1/b)
    
    plt.title("Prior and Posterior Distributions")
    plt.plot(lambda_, prior_pdf, label="Prior: Gamma(a0=1, b0=0.1)", linestyle="dashed")
    plt.plot(lambda_, posterior_pdf, label="Posterior: Gamma(a=44, b=5.1)", linewidth=2)
    plt.xlabel(r"$\lambda$")
    plt.ylabel("Density")
    plt.legend()
    plt.grid()
    plt.show()
    