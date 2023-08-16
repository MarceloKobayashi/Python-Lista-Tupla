from operator import attrgetter

idades = [15, 87, 65, 56, 32, 49, 37]
nomes = ["marcelo", "kenzo", "isabela"]  # letras maiúsculas na frente

nomes_crescentes = sorted(nomes)
print(nomes_crescentes)


class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[Codigo {} Saldo {}]".format(self._codigo, self._saldo)

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False

        return self._codigo == other.codigo and self._saldo == other.saldo

    @staticmethod
    def extrai_saldo(account):
        return account._saldo

    def __lt__(self, other):   # for conta in sorted(contas)
        return self._saldo < other._saldo


conta_marcelo = ContaSalario(1)
conta_marcelo.deposita(500)

conta_kenzo = ContaSalario(2)
conta_kenzo.deposita(1000)

conta_isabela = ContaSalario(3)
conta_isabela.deposita(510)

contas = [conta_marcelo, conta_kenzo, conta_isabela]

for conta in sorted(contas, key=attrgetter("_saldo")):  # obter o saldo
    print(conta)

print(conta_marcelo < conta_isabela)
