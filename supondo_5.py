import os
import time

os.system("cls")

soma = 0

for i in range(4):
    nota = int(input("Digite uma nota: "))
    soma += nota
    
media = soma/ 4

print(f"Média: {media}")