dicionario = {
"primeiro" : {"Nome":"patrick", "Idade": 27},
"segundo" : {"Nome":"lu", "Idade":25},
"terceiro" : {"Nome":"renan", "Idade":33}
}
#1
for key in dicionario:
    print(key)


#2

nome = input("Digite o nome que deseja buscar: ")
novonome = input("Digite o novo nome: ")

for key, valor in dicionario.items():
    if valor["Nome"] == nome:
        dicionario[key]["Nome"] = novonome
       
     #para imprimir a lista atualizada
for key in dicionario:
    print ( dicionario[key]["Nome"])


#3

dicionario["quarto"] = {"Nome": "Rui", "Idade":34}

for key in dicionario:
    print ( dicionario[key]["Nome"])

#4

Pessoa_Remover = input("Inserir a pessoa a eliminar: ")   

if(Pessoa_Remover in dicionario):
    del dicionario[Pessoa_Remover]

print("Dicionário atualizado:")
for key in dicionario:
    print(dicionario[key]["Nome"])  

#5

nomeaproc = input("Digite o nome a procurar: ")

if nomeaproc in [dicionario[key]["Nome"] for key in dicionario]:
    print(f"{nomeaproc} encontrado!")
else:
    print(f"{nomeaproc} não encontrado.")

#6

for key1, key2 in dicionario.items():
    print(f"{key1}: Nome = {key2['Nome']}, Idade = {key2['Idade']}")