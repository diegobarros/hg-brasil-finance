import requests
import config
from datetime import datetime

from models.Cotacao import Cotacao
from dao.sqlite_dao_factory import SqliteDAOFactory

url_base = 'https://api.hgbrasil.com/finance'.format('?key={0}', config.api_key)

def consultar_dados_financeiros(url) -> Cotacao:
    res = requests.get(url_base)
    dados = res.json()['results']['currencies']

    dolar = float(dados['USD']['buy'])
    euro = float(dados['EUR']['buy'])
    data_hora = data = str(datetime.now())

    return Cotacao(dolar, euro, data_hora)


if __name__ == '__main__':
    sqliteFactory = SqliteDAOFactory()
    cotacaoDAO = sqliteFactory.cotacao_dao

    c = consultar_dados_financeiros(url_base)
    cotacaoDAO.adicionar(c)