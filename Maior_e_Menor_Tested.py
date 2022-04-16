
def maior_e_menor(a, b, c):    
    numeros = [a, b, c]
    
    for i in numeros:    
        try: 
            int(i)
        except ValueError:
            return ("Entrada inválida, a entrada não é um número inteiro.")
        if (int(i) < 0) or (int(i) > 1000):  
            return ("Entrada inválida, um ou mais números inseridos não estão entre 0 e 1000.")
    
    # Nesse caso, essas duas condicionais não terão utilidade, portanto esse trecho será comentado
    
    # if (len(numeros) > 5):
    #     return ("Entrada inválida, a quantidade de números inseridos é maior do que cinco.")

    # elif (len(numeros) < 2):
    #     return ("Entrada inválida, a quantidade de números inseridos é menor do que dois.")

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
        return ('O maior número digitado foi %d, e o menor foi %d' % (maior, menor))
