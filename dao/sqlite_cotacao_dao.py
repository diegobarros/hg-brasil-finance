import sqlite3
import dao.sqlite_dao_factory as dao

from dao.cotacao_dao import CotacaoDAO


class SqliteCotacaoDAO(CotacaoDAO):



    def selecionar_cotacao(self, limit=10) -> list:

        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()
        dados =  []
        query = 'SELECT * FROM Cotacao ORDER BY data_hora_coleta LIMIT ?'

        try:
            dados = cursor.execute(query, (limit,)).fetchall()
            conexao.commit()
        except sqlite3.Error as e:
            raise Exception(f'Erro: {e}')
        finally:
            if conexao:
                conexao.close()

        return dados



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
            if conexao:
                conexao.close()

