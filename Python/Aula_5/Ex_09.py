from oper import ler_lista_inteiros, segundo_maior

while True:
    try:
        n = int(input("Quantos valores deseja inserir? "))
        if n > 0:
            break
        else:
            print("Digite um número positivo.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

lista = ler_lista_inteiros(n)

resultado = segundo_maior(lista)

print("\nResultado:")
print(resultado)
