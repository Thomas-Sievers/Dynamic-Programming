pessoa = ("João", 25, "Engenheiro")
print("Tupla (Registro imutável):", pessoa)

#Desempacotamento (útil para clareza)
nome, idade, profissao = pessoa
print(f"Nome = {nome}, Idade = {idade}, Profissão = {profissao}")

#Tupla como chave de dicionário (imutabilidade ajuda)
coordenada = (-3.119, -60.021)
visitas = {coordenada: 5}
print("Visitas por coordenada")