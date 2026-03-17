lista = [10, 20, 30]
print("Lista inicial: ", lista)

lista.append(40)    # Adiciona ao fima da fila
lista[1] = 25       # Modifica o índice 1
lista.remove(30)    # Remove o primeiro valor 30 que achar
print("Lista final: ", lista)

# List comprehension
quadrados = [x*x for x in lista]
print("Quadrados:", quadrados)

#Exemplo prático de lista de compras dinâmicas
compras = ["arroz", "feijão", "macarrão"]
compras.append("leite")

if "sal" not in compras:
    compras.append("sal")
print("Compras:", compras)

#Remover item comprado
compras.remove("arroz")
print("Após a compra do arroz: ", compras)
