import time
import matplotlib.pyplot as plt
import seaborn as sns

def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

def busca_binaria(lista, alvo):
    l, h = 0, len(lista) - 1
    while l <= h:
        m = (l + h) // 2
        if lista[m] == alvo:
            return m
        elif lista[m] < alvo:
            l = m + 1
        else:
            h = m - 1
    return -1

def tempo_processamento_binario(lista):
    tempos_binario = []
    for registro in lista:
        lista_atual = list(range(registro))
        alvo = registro - 1

        inicio_binario = time.perf_counter()
        busca_binaria(lista_atual, alvo)
        final_binario = time.perf_counter()

        tempos_binario.append(final_binario - inicio_binario)
    return tempos_binario


def tempo_processamento_sequencial(lista):
    tempos_sequencial = []
    for registro in lista:
        lista_atual = list(range(registro))
        alvo = registro - 1

        inicio_sequencial = time.perf_counter()
        busca_sequencial(lista_atual, alvo)
        final_sequencial = time.perf_counter()

        tempos_sequencial.append(final_sequencial - inicio_sequencial)
    return tempos_sequencial

tamanhos_arrays = [ 1000, 10000, 50000, 10000]

plt.style.use("fivethirtyeight")
plt.figure(figsize=(10, 6))

sns.lineplot(x=tamanhos_arrays, y=tempo_processamento_sequencial(tamanhos_arrays), label="Busca binária")
sns.lineplot(x=tamanhos_arrays, y=tempo_processamento_sequencial(tamanhos_arrays), label="Busca sequencial")

plt.xlabel("Registros dentro do array")
plt.ylabel("Tempo de processamento")
plt.title("Comparação de desempenho entre busca binária e sequencial")
plt.show()