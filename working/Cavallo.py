import numpy as np
from scipy.stats import poisson
from matplotlib import pyplot as plt

morti = [0,1,2,3,4]
corpi = np.array([109,65,22,3,1])/200
plt.scatter(morti,corpi,color='red',marker='o')

mu = (0*109 + 1*65 + 2*22 + 3*3 + 4*1)/200

dist = poisson(mu)
x = np.arange(0,200,1)
plt.plot(x,dist.pmf(x))
plt.xlim(0,5)
plt.ylim(0,0.7)
plt.show()
