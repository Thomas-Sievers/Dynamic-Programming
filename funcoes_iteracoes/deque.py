from collections import deque

fila = deque(["cliente1", "cliente2", "cliente3"])
print("Fila inicial: ", fila)

fila.append("cliente4")             # Entra no final da fila
fila.appendleft("preferencial")     # Entra no início (esquerda)
atendido = fila.popleft()           # sai do ínicio
print("Atendido: ", atendido)
print("Fila após operações: ", fila)

#Exemplo prático: buffer de 5 sensores
buffer = deque(maxlen=5)
leituras = [10, 12, 15, 11, 13, 17, 19, 18]

for r in leituras :
    buffer.append(r)
    print(f"Nova leitura = {r:2d} -> buffer = {list(buffer)}")