from collections import deque
import statistics as stats

# Pareamento produto-preço e cáculo com total
produtos = ["pão", "leite", "café", "queijo"]
precos = [6.00, 4.80, 15.90, 22.50]

carrinho = list(zip(produtos, precos))
total = sum(preco for _, preco in carrinho)
print("Carrinho: ", carrinho)
print(f"Total: R${total:.2f}")

# Fila de atendimento e relatório
fila = deque(["Aline", "Bruno", "Renato"])
fila.append("Davi")
fila.appendleft("Preferencial: Thomas")

print("Atendimento na ordem: ")
ordem = []
while fila:
    ordem.append(fila.popleft())

for i, nome in enumerate(ordem, start=1):
    print(f"{i:02d}. {nome}")

# Janela deslizante para média móvel
janela = deque(maxlen=3)
dados = [10, 12, 15, 11, 13, 17]

for leitura in dados:
    janela.append(leitura)
    media = stats.mean(janela)
    print(f"Entrada = {leitura:2d} Janela = {list(janela)} Média = {media:5.2f}")