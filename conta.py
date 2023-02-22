
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("COnstruindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do Titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    def transefere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    @property
    def limite(self):
        return self.__limite


