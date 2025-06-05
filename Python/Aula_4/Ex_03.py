lista1 = ["agua","fogo","terra","ar"]
lista2 = ["peixe","calor","minhoca","vento"]

concatenado = lista1 + lista2


existe = input("Digite um elemento para verificar se existe na lista concatenada: ")

if existe in concatenado:
    print("O elemento existe na lista.")
else:
    print("O elemento não existe na lista.")