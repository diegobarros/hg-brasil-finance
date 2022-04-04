import sqlite3
import dao.sqlite_dao_factory as dao
from dao import sqlite_dao_factory
from dao.cotacao_dao import CotacaoDAO


class SqliteCotacaoDAO(CotacaoDAO):

    def adicionar(self, cotacao):

        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()

        query = 'INSERT INTO Cotacao VALUES (null, ?, ?, ?)'
        registro = (cotacao.dolar, cotacao.euro, cotacao.data_hora)

        try:
            cursor.execute(query, registro)
            conexao.commit()
        except sqlite3.Error as e:
            raise Exception(f'Erro: {e}')
        finally:
            conexao.close()

