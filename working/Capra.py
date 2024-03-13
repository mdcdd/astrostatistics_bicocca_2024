import numpy as np

n=0
C=0
N=0
S=0

while (n<10000):
	Tutte = ['Capra','Pecora','Cavolo']
	Due = ['Capra','Pecora','Cavolo']
	Meno = ['Capra','Pecora','Cavolo']
	cons = np.random.choice(Tutte)
	Pres = np.random.choice(['Capra','Pecora'])
	Due.remove(Pres)
	newc = np.random.choice(Due)
	switch = np.random.choice(Tutte)
	Meno.remove(switch)
	if 'Cavolo' in Meno: Meno.remove('Cavolo')
	Pres = np.random.choice(Meno)
	Tutte.remove(Pres)
	switch = np.random.choice(Tutte)

	if cons == 'Cavolo': C=C+1
	if newc == 'Cavolo': N=N+1
	if switch == 'Cavolo': S=S+1
	n = n+1

print('Conservative probability = ',C/n)
print('Newcomer probability = ',N/n)
print('Switcher probability = ',S/n)

