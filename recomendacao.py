avUsuarios = {'Ana': 
		{'Freddy x Jason': 2.5, 
		 'O Ultimato Bourne': 3.5,
		 'Star Trek': 3.0, 
		 'Exterminador do Futuro': 3.5, 
		 'Norbit': 2.5, 
		 'Star Wars': 3.0},
	 
	  'Marcos': 
		{'Freddy x Jason': 3.0, 
		 'O Ultimato Bourne': 3.5, 
		 'Star Trek': 1.5, 
		 'Exterminador do Futuro': 5.0, 
		 'Star Wars': 3.0, 
		 'Norbit': 3.5}, 

	  'Pedro': 
	    {'Freddy x Jason': 2.5, 
		 'O Ultimato Bourne': 3.0,
		 'Exterminador do Futuro': 3.5, 
		 'Star Wars': 4.0},
			 
	  'Claudia': 
		{'O Ultimato Bourne': 3.5, 
		 'Star Trek': 3.0,
		 'Star Wars': 4.5, 
		 'Exterminador do Futuro': 4.0, 
		 'Norbit': 2.5},
				 
	  'Adriano': 
		{'Freddy x Jason': 3.0, 
		 'O Ultimato Bourne': 4.0, 
		 'Star Trek': 2.0, 
		 'Exterminador do Futuro': 3.0, 
		 'Star Wars': 3.0,
		 'Norbit': 2.0}, 

	  'Janaina': 
	     {'Freddy x Jason': 3.0, 
	      'O Ultimato Bourne': 4.0,
	      'Star Wars': 3.0, 
	      'Exterminador do Futuro': 5.0, 
	      'Norbit': 3.5},
			  
	  'Leonardo': 
	    {'O Ultimato Bourne':4.5,
             'Norbit':1.0,
	     'Exterminador do Futuro':4.0}
}

avFilmes = {'Freddy x Jason': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Pedro': 2.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0 },
	 
	 'O Ultimato Bourne': 
		{'Ana': 3.5, 
		 'Marcos': 3.5,
		 'Pedro': 3.0, 
		 'Claudia': 3.5, 
		 'Adriano': 4.0, 
		 'Janaina': 4.0,
		 'Leonardo': 4.5 },
				 
	 'Star Trek': 
		{'Ana': 3.0, 
		 'Marcos:': 1.5,
		 'Claudia': 3.0, 
		 'Adriano': 2.0 },
	
	 'Exterminador do Futuro': 
		{'Ana': 3.5, 
		 'Marcos:': 5.0 ,
		 'Pedro': 3.5, 
		 'Claudia': 4.0, 
		 'Adriano': 3.0, 
		 'Janaina': 5.0,
		 'Leonardo': 4.0},
				 
	 'Norbit': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Claudia': 2.5, 
		 'Adriano': 2.0, 
		 'Janaina': 3.5,
		 'Leonardo': 1.0},
				 
	 'Star Wars': 
		{'Ana': 3.0, 
		 'Marcos:': 3.5,
		 'Pedro': 4.0, 
		 'Claudia': 4.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0}
}

from math import sqrt

def dist(base, key1, key2):
    contItems = {}
    for item in base[key1]:
       if item in base[key2]: contItems[item] = 1

    if len(contItems) == 0: return 0

    soma = sum([pow(base[key1][item] - base[key2][item], 2)
                for item in base[key1] if item in base[key2]])
    return 1/(1 + sqrt(soma))

def getSimilar(base, key):
    similar = [(dist(base, key, other), other)
                    for other in base if other != key]
    similar.sort()
    similar.reverse()
    return similar[0:30]
    
def getRecomend(base, key):
    totais={}
    contSimilar={}
    for other in base:
        if other == key: continue
        similar = dist(base, key, other)

        if similar <= 0: continue

        for item in base[other]:
            if item not in base[key]:
                totais.setdefault(item, 0)
                totais[item] += base[other][item] * similar
                contSimilar.setdefault(item, 0)
                contSimilar[item] += similar
    rankings=[(total / contSimilar[item], item) for item, total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings[0:30]
                
def baseML(path='C:/ml-100k'):
    filmes = {}
    for linha in open(path + '/u.item'):
        (id, titulo) = linha.split('|')[0:2]
        filmes[id] = titulo
    # print(filmes)

    base = {}
    for linha in open(path + '/u.data'):
        (user, idfilme, nota, tempo) = linha.split('\t')
        base.setdefault(user, {})
        base[user][filmes[idfilme]] = float(nota)
    return base            

def setItems(base):
    result = {}
    for item in base:
        notas = getSimilar(base, item)
        result[item] = notas
    return result

def getItems(base, similaridadeItens, usuario):
    notasUsuario = base[usuario]
    notas={}
    totalSimilaridade={}
    for (item, nota) in notasUsuario.items():
        for (similaridade, item2) in similaridadeItens[item]:
            if item2 in notasUsuario: continue
            notas.setdefault(item2, 0)
            notas[item2] += similaridade * nota
            totalSimilaridade.setdefault(item2,0)
            totalSimilaridade[item2] += similaridade
    rankings=[(score/totalSimilaridade[item], item) for item, score in notas.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
        


























