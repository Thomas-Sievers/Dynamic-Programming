def busca_binaria_while(lista, m):
    inicio, fim = 0, len(lista) - 1
    i = 0

    while inicio <= fim:
        i =+ 1
        m = (inicio + fim) // 2
        print(f"Iteração {i}: inicio = {inicio}, fim = {fim}, alvo = {m}")
        if lista[m] == alvo:
            return m
        elif lista[m] < alvo:
            inicio = m + 1
        else:
            fim = m - 1
    return -1

def busca_binaria_for(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    for i in range(len(lista)):
        m = (inicio + fim) // 2
        print(f"Iteração: {i + 1}: inicio = {inicio}, fim = {fim}, alvo = {m}")
        if inicio > fim:
            break
        if lista[m] == alvo:
            return m
        elif lista[m] > alvo:
            inicio = m + 1
        else:
            fim = m - 1
    return -1

lista = [11, 17, 18, 45, 50, 71, 95]
alvo = 50
resultado_while = busca_binaria_while(lista, alvo)
resultado_for = busca_binaria_for(lista, alvo)

print(f"Índice do alvo: {resultado_while}")