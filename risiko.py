import numpy as np
from itertools import product


	
def ordinecombinazione(x):
	return np.sort(np.array(x))[::-1]

def probabilitaAttacoDifesa(nfacce,ndaddi):
	combinazioni=[list(c) for c in product(range(1, nfacce+1), repeat=ndaddi)]#generazione di tutte le conbinazioni con numero di daddi e facce del daddo selezionate 

	attack=ordinecombinazione(combinazioni)
	defense=ordinecombinazione(combinazioni)


	ris= np.zeros(ndaddi+1) 
	
	for a in attack:
		for d in defense:
			resatt=0
			#print(a,d)
			for c in range(ndaddi):
				
				if a[c]>d[c]:#attaco positivo
					resatt+=1
				
	
			
			
			for i in range (ndaddi+1):
				if resatt==i:
					ris[i]+=1

	totcomb=nfacce**(2*ndaddi)
	sommadaddi=sum(ris)
	
	if (totcomb==sommadaddi):
		for i in range(ndaddi+1):
			print(f'attaco perde{i}, difesa perde{daddi-i} e di {ris[i]} o {ris[i]/sommadaddi:.2f}')
	else:
		print('err')


	


if __name__ == "__main__":
	N=10#numero facce daddo
	dice=2

	probabilitaAttacoDifesa(N,dice)

