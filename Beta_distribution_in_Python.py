import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Set the shape paremeters

a, b = 80, 10

# Generate the value between

x = np.linspace (beta.ppf (0.01, a, b), beta.ppf (0.99, a, b), 100)

# Plot the beta distribution

plt.figure (figsize = (7, 7))
plt.xlim (0.7, 1)
plt.plot (x, beta.pdf (x, a, b), 'r-')
plt.title ('Beta Distribution', fontsize = '15')
plt.xlabel ('Values of Random Variable X (0, 1)', fontsize = '15')
plt.ylabel ('Probability', fontsize = '15')
plt.show ()