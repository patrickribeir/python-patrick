frase = str(input("insira uma frase: "))

palavra = str(input("insira uma palavra: "))

inicio = "Olá"
Fim = "!"

# Verifica se a palavra está na frase
if palavra in frase:
    print(f"A palavra {palavra} está na frase")
else:
    print("A palavra não está na frase")

# substitui os espacos por -
print (frase.replace(" ", "-"))

# verificar se comeca por ola ou termina com !
if frase.startswith(inicio):
    print("A frase começa com 'Olá'")
    if frase.endswith(Fim):
        print("Termina com '!'")
    


