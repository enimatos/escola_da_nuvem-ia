try:
    idade = int(input("Digite a sua idade: "))
    if idade < 0:
        raise ValueError("Idade nao pode ser negativa")
    print(f"Sua idadevé: {idade}")
except ValueError as error:
    print(f"Erro: {error}")