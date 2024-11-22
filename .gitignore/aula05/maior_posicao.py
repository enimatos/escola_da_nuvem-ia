import random


valor = [random.randint(1,10000) for _ in range(100)]

maior = (max(valor))
posicao = valor.index(maior)

resultado = {
    "Numeros": valor,
    "Maior Valor": maior,
    "Posicao": posicao
}

print("\n Números gerados:")
print("\n Números gerados:")
print(f"\n Maior Valor:", maior)
print("\nPosição de Maior valor :", posicao)