frutas = ["nectarina", "pera", "abacaxi", "mamao", "caju"]


#numero de letras de cada palavra

numletras = {len(fruta) for fruta in frutas}

print (numletras)

#numero de letras de cada palavra + nome da fruta

numletras = {fruta: len(fruta) for fruta in frutas}

print (numletras)