string = ''' essa é uma frase de teste
do curso de py no cesae digital, no fim desse curso vou estar
pronto para o mercado de trabalho, isso se eu passar no exame final da 
AWS, vamos ver né... tomara que sim '''

palavra = str(input("insira uma paravra para eu verificar se esta no meu texto secreto: "))

if palavra in string:
    print ("a palavra está no texto")

else:
    print ("a palavra não está no texto")

    