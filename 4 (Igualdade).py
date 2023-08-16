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


conta1 = ContaSalario(1)
conta2 = ContaSalario(1)
print(conta1, conta2)
print(conta1._saldo == conta2._saldo)
