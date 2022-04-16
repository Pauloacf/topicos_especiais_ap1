def main():
    print('MAIOR E MENOR NÚMERO')
    print('--------------------')
    numeros = input('Digite dois a cinco números de 0 a 1000: ').split(',')
    
    for i in numeros:    
        try: 
            int(i)
        except ValueError:
            print("Entrada inválida, a entrada não é um número inteiro.")
            return
        if (int(i) < 0) or (int(i) > 1000):  
            print("Entrada inválida, um ou mais números inseridos não estão entre 0 e 1000.")
            return
    if (len(numeros) > 5):
        print("Entrada inválida, a quantidade de números inseridos é maior do que cinco.")

    elif (len(numeros) < 2):
        print("Entrada inválida, a quantidade de números inseridos é menor do que dois.")

    else:
        count = 0
        maior = 0
        menor = int(numeros[0])
        while (count < len(numeros)):
            if(int(numeros[count]) > maior):
                maior = int(numeros[count])
            elif(int(numeros[count]) < menor):
                menor = int(numeros[count])
            count += 1
        print('O maior número digitado foi %d, e o menor foi %d' % (maior, menor))
main()