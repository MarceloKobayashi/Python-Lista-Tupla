from abc import ABCMeta, abstractmethod


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[Codigo {} Saldo {}]".format(self._codigo, self._saldo)

    @abstractmethod
    def passa_o_mes(self):  # todas as sublasses tem que ter um metodo passa o mes
        pass


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaInvestimento(Conta):
    def passa_o_mes(self):
        pass
