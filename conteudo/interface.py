import customtkinter as ctk
import tkinter as tk

def interface():
    pass

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

tempoDeUso = ctk.CTkLabel(janela, text = 'TEMPO DE USO ATÉ A PARADA')
tempoDeUso.grid(row = 1, column = 3, padx = 40, pady = 20)
caixa_tempo = ctk.CTkEntry(janela, placeholder_text= 'D/H/M (só números)')
caixa_tempo.grid(row = 1, column = 4, padx = 40, pady = 20)

data = ctk.CTkLabel(janela, text = 'DATA DA MANUTENÇÃO')
data.grid(row = 2, column = 3, padx = 40, pady = 20)
caixa_data = ctk.CTkEntry(janela, placeholder_text='Data em D/M/A')
caixa_data.grid(row = 2, column = 4, padx = 40, pady = 20)

ocor = ctk.CTkLabel(janela, text= 'TIPO DE OCORRÊNCIA')
ocor.grid(row = 4, column = 0, padx = 40, pady = 20)
caixa_ocor = ctk.CTkOptionMenu(janela, values=['MECÂNICA', 'ELÉTRICA', 'AUTOMAÇÃO', 'TROCA DE PEÇA'])
caixa_ocor.grid(row = 4, column = 1, padx = 40, pady = 20)

botEnviar = ctk.CTkButton(janela, text='ENVIAR DADOS', fg_color='#8B008B', command=True)
botEnviar.grid(row = 4, column = 3, padx = 40, pady = 20)

botRelat = ctk.CTkButton(janela, text='RELATÓRIOS', fg_color='#8B0000' , command=True)
botRelat.grid(row = 4, column = 4, padx = 40, pady = 20)






janela.mainloop()

