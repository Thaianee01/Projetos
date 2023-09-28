import os
import time

os.system('cls')

print ("Calculadora\n")

while True:
    operação = input('Escolha um operador matemático para o calculo: soma (+), subtração (-), multiplicação (*), divisão (/). Digite "fim", para sair do programa.')
    
    if operação == "fim":
        print ("saindo da calculadora...")
        break
    
    if operação == "+":
        print ("Você escolheu soma")
    
    elif operação == "-":
        print ("Você escolheu subtração")
    
    elif operação == "*":
        print ("Você escolheu multiplicação")
    
    elif operação == "/":
        print ("Você escolheu divisão")
    
    else:
        print ("Operação inválida")
        continue
    
    n1 = float(input("Digite o numero que deseja fazer a operação = "))
    n2 = float(input("Digite o numero que deseja fazer a operação = "))
        
    if operação == "+":
        soma = (n1 + n2)
        print ("calculando...")
        time.sleep (1)
        print ("==============")
        print (soma)
        
    if operação == "-":
        subtração = (n1 - n2)
        print ("calculando...")
        time.sleep (1)
        print ("==============")
        print (subtração)
        
    if operação == "*":
        multiplicação = n1 * n2
        print ("calculando...")
        time.sleep (1)
        print ("==============")
        print (multiplicação)
        
    if operação == "/":
        divisão = n1 / n2
        time.sleep (1)
        print ("calculando...")
        print ("==============")
        if n2 == 0:
            print ("erro, não é possivel dividir por zero")
        else:
            print (divisão)

