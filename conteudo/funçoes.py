import sqlite3


def enviar_dados():
    conexao = sqlite3.connect('BaseDeDados.db')
    curso = conexao.cursor()
    curso.execute('INSERT INTO BaseDeDados VALUES (:SETOR, :MÁQUINA, :OPERADOR, :TÉCNICO, :TEMPO DE USO ATÉ A PARADA, :DATA DA MANUTENÇÃO, :TIPO DE OCORRÊNCIA)',
                  {
                      'SETOR': entrysetor
                      'MÁQUINA'
                      'OPERADOR'
                      'TÉCNICO'
                      'TEMPO DE USO ATÉ A PARADA'
                      'DATA DA MANUTENÇÃO'
                      'TIPO DE OCORRÊNCIA'





                  }
                  )
    pass