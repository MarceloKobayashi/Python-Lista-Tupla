from operator import attrgetter
from functools import total_ordering

nomes = ["marcelo", "kenzo", "isabela"]  # letras maiúsculas na frente

nomes_crescentes = sorted(nomes)
print(nomes_crescentes)


@total_ordering   # possibilidade de <=
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

        return self._codigo == other._codigo and self._saldo == other._saldo

    @staticmethod
    def extrai_saldo(account):
        return account._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo


conta_marcelo = ContaSalario(100)
conta_marcelo.deposita(500)

conta_kenzo = ContaSalario(2)
conta_kenzo.deposita(1000)

conta_isabela = ContaSalario(3)
conta_isabela.deposita(500)

contas = [conta_marcelo, conta_kenzo, conta_isabela]

for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):  # se o saldo for igual, o codigo desempata
    print(conta)

print(conta_isabela <= conta_marcelo)
