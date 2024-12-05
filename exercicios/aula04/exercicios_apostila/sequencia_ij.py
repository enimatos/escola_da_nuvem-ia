i, j = 1,60

while j>0:
    print(f"I={i} J={j}")
    i += 3
    j -= 5

#criar a mesma lógica em função

def sequenciar(a,b):
    while b>0:
        print(f"I={a} J={b}")
        a += 3
        b -= 5


sequenciar(1,60)