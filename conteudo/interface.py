import customtkinter as ctk
import sqlite3
import pandas as pd
import openpyxl

def enviar_dados():
    conexao = sqlite3.connect('BaseDeDados.db')
    curso = conexao.cursor()
    curso.execute('INSERT INTO dados VALUES (:SETOR, :MÁQUINA, :OPERADOR, :TÉCNICO, :TEMPO_PARADA, :DATA_OCORRÊNCIA, :TIPO_OCORRÊNCIA)',
                {     'SETOR':caixa_setor.get(),
                      'MÁQUINA':caixa_maq.get(),
                      'OPERADOR':caixa_operad.get(),
                      'TÉCNICO':caixa_tecn.get(),
                      'TEMPO_PARADA':caixa_tempo.get(),
                      'DATA_OCORRÊNCIA':caixa_data.get(),
                      'TIPO_OCORRÊNCIA':caixa_ocor.get()
                }
                )
    
    conexao.commit()
    conexao.close()

    caixa_setor.delete(0, 'end')
    caixa_maq.delete(0, 'end')
    caixa_operad.delete(0, 'end')
    caixa_tecn.delete(0, 'end')
    caixa_tempo.delete(0, 'end')
    caixa_data.delete(0, 'end')

def excel():
    conexao = sqlite3.connect('BaseDeDados.db')
    curso = conexao.cursor()

    curso.execute('SELECT * FROM dados')

    dados_cadastrados = curso.fetchall()

    dados_cadastrados = pd.DataFrame(dados_cadastrados, columns=['SETOR','MÁQUINA','OPERADOR','TÉCNICO','TEMPO_PARADA','DATA_OCORRÊNCIA','TIPO_OCORRÊNCIA'])

    dados_cadastrados.to_excel('DADOS.xlsx')

    conexao.commit()

    conexao.close()


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

janela = ctk.CTk()
janela.title('Manutenção')
janela.minsize(900, 400)
janela.maxsize(900, 400)

setor = ctk.CTkLabel(janela, text= 'SETOR')
setor.grid(row = 0, column = 0, padx = 40, pady = 20)
caixa_setor = ctk.CTkEntry(janela, placeholder_text= 'Setor atendido')
caixa_setor.grid(row = 0, column = 1, padx = 40, pady= 20)

maq = ctk.CTkLabel(janela, text= 'MÁQUINA')
maq.grid(row = 1, column = 0, padx = 40, pady = 20)
caixa_maq = ctk.CTkEntry(janela, placeholder_text= 'Máquina atendida')
caixa_maq.grid(row = 1, column = 1, padx = 40, pady = 20)

operad = ctk.CTkLabel(janela, text= 'OPERADOR')
operad.grid(row = 2, column = 0, padx = 40, pady = 20)
caixa_operad = ctk.CTkEntry(janela, placeholder_text= 'Operador da máquina')
caixa_operad.grid(row = 2, column = 1, padx = 40, pady = 20)

tecn = ctk.CTkLabel(janela, text = 'TÉCNICO')
tecn.grid(row = 0, column = 3, padx = 40, pady = 20)
caixa_tecn = ctk.CTkEntry(janela, placeholder_text= 'Técnico operante')
caixa_tecn.grid(row = 0, column = 4, padx = 40, pady = 20)

tempoDeUso = ctk.CTkLabel(janela, text = 'Tempo de máquina parada')
tempoDeUso.grid(row = 1, column = 3, padx = 40, pady = 20)
caixa_tempo = ctk.CTkEntry(janela, placeholder_text= '12H34M')
caixa_tempo.grid(row = 1, column = 4, padx = 40, pady = 20)

data = ctk.CTkLabel(janela, text = 'DATA DA MANUTENÇÃO')
data.grid(row = 2, column = 3, padx = 40, pady = 20)
caixa_data = ctk.CTkEntry(janela, placeholder_text='Data em D/M/A')
caixa_data.grid(row = 2, column = 4, padx = 40, pady = 20)

ocor = ctk.CTkLabel(janela, text= 'TIPO DE OCORRÊNCIA')
ocor.grid(row = 4, column = 0, padx = 40, pady = 20)
caixa_ocor = ctk.CTkOptionMenu(janela, values=['MECÂNICA', 'ELÉTRICA', 'AUTOMAÇÃO', 'TROCA DE PEÇA'])
caixa_ocor.grid(row = 4, column = 1, padx = 40, pady = 20)

botEnviar = ctk.CTkButton(janela, text='ENVIAR DADOS', fg_color='#8B008B', command= enviar_dados)
botEnviar.grid(row = 4, column = 3, padx = 40, pady = 20)

botRelat = ctk.CTkButton(janela, text='EXCEL', fg_color='#8B0000' , command=excel)
botRelat.grid(row = 4, column = 4, padx = 40, pady = 20)

janela.mainloop()

