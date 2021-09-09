from math import sqrt as rc
retry = 1

def nombrePremier(nb):
	result = []
	while nb != 1:
		premier = False

		a = 2
		while not premier:
			if nb % a == 0:
				nb = nb / a
				result.append(int(a))
				premier = True
			else:
				a += 1

	return(result)

def diviseur(nbx):
	listdiviseur = []
	for i in range(1, nbx + 1):
			if nbx % i == 0:
					listdiviseur += [i]
	return(listdiviseur)
    				

while retry:
	numb = int(input("Number to decompose: "))
	resultat = nombrePremier(numb)
	resultatscd = diviseur(numb)
	print(resultat)
	print(resultatscd)
	retry = bool(int(input("do you want to retry (0/1)?")))