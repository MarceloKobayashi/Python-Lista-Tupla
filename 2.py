class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[Codigo {} Saldo {}]".format(self.codigo, self.saldo)

    def deposita_para_todas(self):
        for conta in self.codigo:
            conta += 100

    def deposita_tupla(self, conta):
        novo_saldo = conta[1] + 100
        codigo = conta[0]
        return "[Codigo {} Saldo {}]".format(codigo, novo_saldo)


conta_marcelo = ContaCorrente(1)
conta_marcelo.deposita(500)
conta_ana = ContaCorrente(2)
conta_ana.deposita(1000)

sla = conta_marcelo.deposita_tupla((1, 1000))

contas = (sla, conta_ana)
for conta in contas:
    print(conta)
