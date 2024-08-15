import sqlite3


conexao = sqlite3.connect('BaseDeDados.db')

curso = conexao.cursor()

curso.execute('''
    CREATE TABLE dados (
              SETOR text,
              MÁQUINA text,
              OPERADOR text,
              TÉCNICO text,
              TEMPO_PARADA text,
              DATA_OCORRÊNCIA text,
              TIPO_OCORRÊNCIA text
              )
''')

conexao.commit()

conexao.close()