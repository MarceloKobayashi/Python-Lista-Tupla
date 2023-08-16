idades = list()


def adiciona(ages):
    ages.append(10)
    ages.append(20)
    ages.append(30)
    ages.append(40)
    print(ages)
    print(len(ages))
    if 10 in ages:
        ages.remove(10)
    ages.insert(0, 50)
    print(ages)
    ages.extend([60, 70])
    print(ages)


def somar(ages):
    nova_lista = [(age + 1) for age in ages]
    print(nova_lista)


def visualizacao(lista=None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)


sla = adiciona(idades)
naosei = somar(idades)
for idade in idades:
    print(idade)
