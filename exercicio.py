import os
import time

os.system("cls")
numero = int(input("Digite um numero da tabuada: "))


print(f"\nTabuada de {numero}: ")
print("_" * 15)

# range(1, 11) vai de 1 até 10 (*o último numero é exclusivo)
for i in range(1, 11):
    
    resultado = numero * i
    #f-string para formatar a saida d forma organizada
    print(f"{numero} x {i} = {numero * i}")
    print("-" * 15)

