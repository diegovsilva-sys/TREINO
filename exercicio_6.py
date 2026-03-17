import os
import time

os.system("cls")

soma = 0
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTA):
 nota = float(input("Digite a nota: "))

 soma += nota
 media = soma / QUANTIDADE_NOTA

if media >= 7:
    resultado = "Aprovado"
    
elif media <= 4:
    resultado = "Reprovado"
    
else:
    resultado = "Recuperação"

print(f"Media: {media}")
print(f"Resultado: {resultado}")