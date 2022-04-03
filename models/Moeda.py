class Moeda:

    def __init__(self, dolar: float, euro: float, data_hora: str) -> None:
        super().__init__()
        self.__dolar = dolar
        self.__euro = euro
        self.__data_hora = data_hora

    @property
    def dolar(self):
        return self.__dolar

    @property
    def euro(self):
        return self.__euro

    @property
    def data_hora(self):
        return self.__data_hora


    @property
    def cotacao(self) -> dict:
        return {
            'dolar': self.__dolar,
            'euro': self.__euro,
            'data_hora': self.__data_hora
        }