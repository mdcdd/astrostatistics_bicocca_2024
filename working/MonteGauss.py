import numpy as np
from matplotlib import pyplot as plt

N = 10000
Samples = np.arange(100,10000,50)

fig, graph = plt.subplots(2)

for S in Samples:
	x = np.random.uniform(0,N,S)
	sigma = np.std(x)

	f = (x**3)*np.exp(-(x**2)/(2*(sigma**2)))

	integral = N*np.mean(f)

	theory = 2*(sigma**4)

	error = theory - integral
	graph[0].scatter(S,integral,color='r',marker='^')
	graph[0].scatter(S,theory,color='k',marker='.')
	graph[1].scatter(S,error/integral)

plt.show()
#print("Valore: ", integral)
#print("Teorico: ", theory)
#print("Errore: ", error)
