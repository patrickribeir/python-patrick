lista = [x ** 2 for x in range (10)]        

print(lista)

#para criar dicionario

dicionariolista = {x : x ** 2 for x in range (10)}

print(dicionariolista)

#para criar dicionario e imprimir apenas os pares

dicionariolistapares = {x : x ** 2 for x in range (10) if x % 2 == 0}

print(dicionariolistapares)

#para criar dicionario e imprimir os pares e impares
teste = {x : "par" if x % 2 == 0 else "impar" for x in range (10)}

print (teste)