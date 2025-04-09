opcao = int(input("Selecione a operação desejada. \n 1 -Criar \n 2 - Atualizar \n 3 - Eliminar \n 4 - Sair \n"))

if opcao == 1:
    nome = str(input("Informe o nome a criar: "))
    print (f"O nome foi criado {nome}")

elif opcao == 2:
    nome = str(input("Informe o novo nome: "))
    print (f"O nome foi atualizado com sucesso {nome}!")

elif opcao == 3:
    print( "O seu registro foi eliminado com sucesso!")

elif opcao == 4:
    print ("Bem vindo a pagina inicial")


else:
    print ("Selecionou uma opcao invalida")