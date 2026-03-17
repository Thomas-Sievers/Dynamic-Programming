from collections import deque

valores = [10, 15, 20, 25, 30]

# map: aplicar 10% de desconto
com_desconto = list(map(lambda x: x*0.9, valores))  # O map aplica uma função para cada elemento
print("Com 10% de desconto:", com_desconto)

# filter: manter apenas valores >=
maiores_ou_iguais_20 = list(filter(lambda x: x >= 20, valores))  # Mantém apenas valores que atendem uma condição
print(">= 20:", maiores_ou_iguais_20)

# Com deque funciona do mesmo modo
fila = deque([1, 2, 3, 4])
dobro = deque(map(lambda x: x*2, fila))
print("Dobro: ", dobro)
maiores_que_2 = deque(filter(lambda x: x > 2, fila))
print("Maiores que 2: ", maiores_que_2)