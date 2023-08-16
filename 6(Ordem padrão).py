idades = [15, 87, 65, 56, 32, 49, 37]

ordem_crescente = sorted(idades)
print(ordem_crescente)

ordem_decrescente = sorted(idades, reverse=True)  # ou list(reversed(sorted(idades)))
print(ordem_decrescente)

ordem_inversa = list(reversed(idades))
print(ordem_inversa)

ordem_crescente2 = idades.sort()
print(idades)
