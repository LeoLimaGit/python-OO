class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))


data = Data(23, 12, 2002)
data2 = Data(23, 12, 2002)
data3 = Data(23, 12, 2002)
data4 = Data(23, 12, 2002)

data.formatada(23, 12, 2002)
data2.formatada(23, 12, 2002)
data3.formatada(23, 12, 2002)
data4.formatada(23, 12, 2002)
