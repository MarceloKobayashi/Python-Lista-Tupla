idades = [15, 87, 65, 56, 32, 49, 37]

for i in range(len(idades)):
    print(i, idades[i])

lista = list(enumerate(idades))
print(lista)
for indice, idade in enumerate(idades):
    print(indice, "-", idade)

usuarios = [
    ("marcelo", 1, 2004),
    ("kenzo", 2, 2005),
    ("isabela", 3, 2006)
]
for nome, _, _ in usuarios:
    print(nome)
