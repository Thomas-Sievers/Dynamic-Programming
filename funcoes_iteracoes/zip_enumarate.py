produtos = ["arroz", "feijão", "leite", "ovos"]
precos = [6.50, 9.99, 4.80, 12.00]

#zip -> pares produto-preço
for produto, preco in zip(produtos, precos):
    print(f"{produto:7s} -> {preco:,.2f}")

#enumarate -> índice + valor (útil para etiquetas, ranking e etc)
for i, produto in enumerate(produtos, start=1):
    print(f"#{i}: {produto}")