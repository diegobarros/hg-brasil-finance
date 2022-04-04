from abc import ABC, abstractmethod


class CotacaoDAO(ABC):

    @abstractmethod
    def adicionar(self, cliente):
        pass

    @abstractmethod
    def selecionar_cotacao(self, limit=10) -> list:
        pass

#    @abstractmethod
#    def excluir(self, id):
#        pass

#    @abstractmethod
#    def pesquisar(self, data_hora):
#        pass
