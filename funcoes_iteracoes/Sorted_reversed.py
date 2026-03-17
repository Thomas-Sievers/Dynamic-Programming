dados = [("arroz", 6.50), ("ovos", 12.00), ("leite", 4.80), ("feijão", 9.99)]

#Ordenar por preço (2 elemento)
por_preco = sorted(dados, key=lambda par: par[1])
print("Ordenado por preço: ", por_preco)

#Ordenar por nome desc
por_nome_desc = sorted(dados, key=lambda par: par[0], reverse=True)
print("Ordenado por nome decrescente: ", por_nome_desc)

#Reversed
lista = [1, 2, 3, 4]
print("Reversed: ", list(reversed(lista)))
