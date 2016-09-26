import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math

mu = 10
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(0, 24, 200)
plt.plot(x,2.5*mlab.normpdf(x, mu, sigma))

plt.show()