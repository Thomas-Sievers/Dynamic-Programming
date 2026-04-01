 # Library to normalize strings
from unidecode import unidecode

# Linear Search using numbers
lista = [2, 3, 4, 10, 40]
alvo = 10

def busca_linear_for(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -100

def busca_linear_while(lista, alvo):
    i = 0
    while i < len(lista):
        if lista[i] == alvo:
            return i
        i += 1
    return - 100

resultado_for = busca_linear_for(lista, alvo)
resultado_while = busca_linear_while(lista, alvo)

if resultado_for != -100 and resultado_while != -100:
    print(f"O {alvo} foi enontrado no ínidicce {resultado_for} usando o loop for")
    print(f"O {alvo} foi enontrado no ínidicce {resultado_while} usando o loop while")

# Linear search using Strings (we can use the functions above to strings too)
produtos = ["Arroz", "feijão", "açucar", "café", "Óleo"]
produto_procurado = "café"

def procura_normalizando_string(lista, alvo):
    alvo_normalizado = unidecode(alvo).lower()
    for i in range(len(lista)):
        produto_normalizado = unidecode(lista[i]).lower()

        if produto_normalizado == alvo_normalizado:
            return i
    else:
        return -100

# Normalizing the strings
resultado_string_for = procura_normalizando_string(produtos, produto_procurado)
print(resultado_string_for)

