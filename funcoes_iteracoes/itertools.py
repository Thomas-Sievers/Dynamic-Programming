import itertools

a = [1, 2]
b = [3, 4]

print("Chain: ", list(itertools.chain(a, b)))

#islice: pegar 5 elementos de um gerador
gen = (x*x for x in range(10000))
primeiros_cinco = list(itertools.islice(gen, 5))
print("Primeiros 5 quadrados: ", primeiros_cinco)

#Cycle: repetir o padrão 3x
padrao = ["A", "B", "C"]
ciclo = itertools.cycle(padrao)
repeticao_controlada = [next(ciclo) for _ in range(9)]
print("Cycle (3 voltas): ", repeticao_controlada)