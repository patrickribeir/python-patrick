texto = "esse é um texto teste pra descobrir quais palavras tem menos de 4 letras, vamos ver,, o que vai dar"

menosq4 = [palavra.strip(',') for palavra in texto.split() if len(palavra.strip(',')) <= 4 ]

print(menosq4)