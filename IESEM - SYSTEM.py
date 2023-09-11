# AULA 1: CRIANDO JANELA
import reportlab
import sys
import time
# importando configurações da janela
from tkinter import *

from tkinter import Scrollbar
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import END
from tkinter import Frame
from tkinter import ttk
# Mensagem de Aviso
from tkinter import messagebox
from datetime import datetime
# importando configurações do pdf

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import os
# importando configurações do navegador
import webbrowser

dd = datetime.now()
date_today = dd.date()
hoje = date_today.strftime("%d/%m/%Y")

def progress_bar(done):
    print("\rCarregando: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100), end='')
    
def test():
    for n in range(101):
        progress_bar(n/100)
        time.sleep(0.1)
        
test()

CURSOR_POSITIONS = ('\\', '|', '/', '-')
CURRENT_CURSOR_POS = 0

print("")
print(" ______________ ____________________   _____      ___________________ _______________________________   _____    ")
print("|   \_   _____//   _____/\_   _____/  /     \    /   _____/\__  |   |/   _____/\__    ___/\_   _____/  /     \   ")
print("|   ||    __)_ \_____  \  |    __)_  /  \ /  \   \_____  \  /   |   |\_____  \   |    |    |    __)_  /  \ /  \  ")
print("|   ||        \/        \ |        \/    Y    \  /        \ \____   |/        \  |    |    |        \/    Y    \ ")
print("|___/_______  /_______  //_______  /\____^__  / /_______  / / ______/_______  /  \____|   /_______  /\____^__  / ")
print("            \/        \/         \/         \/          \/  \/              \/                    \/         \/  ")
print("")
print("By Helan S.Gonçalves")
print("Programmer")
print("")
print("")


root = Tk()
# importando configurações do banco
import sqlite3

class GeneratePDF():
    def variable(self):
        # get para pegar do input
        self.name = self.input_name.get()
        self.search_name = self.input_search_name.get()
        self.cell = self.input_cell.get()
        self.turma = self.Tipvar1.get()
        self.pay = self.Tipvar2.get()
        self.month = self.Tipvar3.get()
        self.year = self.input_year.get()
        self.pago = "R$ " + self.input_money.get()
        self.data = str("{}/{}".format(self.month, self.year))
        # self.name_file = "{} {}".format(self.search_name, self.data)      
    def printReceipt(self):
        # self.variable()
        webbrowser.open("Comprovante.pdf")

    def generateReceipt(self):
        self.variable()
        if self.input_year.get() == "":
            print("\nAviso!! - Comprovante:\n")
            print("Preencha o formulário abaixo para")
            print("poder gerar o comprovante do aluno:")
            print("\n=> Nome \n=> Forma de Pagamento \n=> Mês \n=> Ano \n=> Valor pago no mês")
            msg = "Preencha corretamente o formulário abaixo para \n"
            msg += "poder gerar o comprovante do aluno"
            # CAIXA DE TEXTO
            messagebox.showinfo("Aviso!! - Comprovante", msg)
        elif self.input_money.get() == "":
            print("\nAviso!! - Comprovante:\n")
            print("Preencha o formulário abaixo para")
            print("poder gerar o comprovante do aluno:")
            print("\n=> Nome \n=> Forma de Pagamento \n=> Mês \n=> Ano \n=> Valor pago no mês")
            msg = "Preencha corretamente o formulário abaixo para \n"
            msg += "poder gerar o comprovante do aluno"
            # CAIXA DE TEXTO
            messagebox.showinfo("Aviso!! - Comprovante", msg)
        else:
            def _get_next_cursor():
                global CURRENT_CURSOR_POS
                try:
                    CURRENT_CURSOR_POS += 1
                    return CURSOR_POSITIONS[CURRENT_CURSOR_POS]
                except:
                    CURRENT_CURSOR_POS = 0
                    return CURSOR_POSITIONS[CURRENT_CURSOR_POS]
                
            def spinning_cursor_with_label(label_text):
                sys.stdout.write('\r[{}]\t{}'.format(_get_next_cursor(), label_text))
                sys.stdout.flush()


            for i in range(101):
                time.sleep(0.1)
                spinning_cursor_with_label(label_text="Editando PDF {}%...".format(i))
            print("")
            print("\nATENÇÃO!! => Quando o comprovante for gerado no navegador")
            print("Copie um arquivo do mesmo para um certo diretório e renomeie da seguinte forma:")
            print("")
            pastaApp=os.path.dirname(__file__)
            self.c = canvas.Canvas("Comprovante.pdf")
            self.NAMERel = self.search_name
            self.VALUErRel = self.pago
            self.FORM_PAYRel = self.pay
            self.DATARRel = self.data
            print("Ex: Helan Sousa Gonçalves_Básico_202309")
            # Titulo
            self.c.setFont("Helvetica", 16)
            self.c.drawString(65, 720, 'RECIBO IESEM')
            self.c.drawImage(pastaApp+"\\IESEM_Comprovante.png", 400, 690)
            
            #Imagem
            
            
            # Info
            self.c.setFont("Helvetica", 12)
            self.c.drawString(65, 635, 'Recebemos de:')
            self.c.drawString(65, 610, 'A importância de:')
            self.c.drawString(65, 585, 'Referente: Mensalidade')
            self.c.drawString(65, 560, 'Mês:')
            self.c.drawString(65, 510, '_' * 30)
            self.c.drawString(85, 495, 'ASSINATURA SECRETARIA')
            
            self.c.drawString(280, 610, 'Forma de pagamento:')
            self.c.drawString(280, 560, 'Emitente: Paula Baptista Amaral')
            self.c.drawString(360, 510, 'Data de Emissão:')
            
            self.c.setFont("Helvetica", 12)
            self.c.drawString(155, 635, self.NAMERel)
            self.c.drawString(165, 610, self.VALUErRel)
            self.c.drawString(95, 560, self.DATARRel)
            self.c.drawString(402, 610, self.FORM_PAYRel)
            self.c.drawString(457, 510, hoje)
    
            self.c.showPage()
            self.c.save()
            self.printReceipt()


      
class Function():   
    def variable(self):
        # get para pegar do input
        self.name = self.input_name.get()
        self.search_name = self.input_search_name.get()
        self.cell = self.input_cell.get()
        self.turma = self.Tipvar1.get()
        self.pay = self.Tipvar2.get()
        self.month = self.Tipvar3.get()
        self.year = self.input_year.get()
        self.pago = "R$ " + self.input_money.get()
        self.data = str("{}/{}".format(self.month, self.year))
        # self.name_file = "{} {}".format(self.search_name, self.data)

    def Delete1(self):
        self.input_search_name.delete(0, END)
        self.input_year.delete(0, END)
    # OK
    def Delete2(self):
        self.input_name.delete(0, END)
        self.input_cell.delete(0, END)
        
    # OK
    def ativarState(self):
        self.input_search_name.config(state="normal")
        
    def desativarState(self):
        self.input_search_name.config(state="readonly")
        
    def conecta_bd(self):
        self.conn = sqlite3.connect("Aluno.bd")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados...")
    # OK 
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados...")
    
    # OK
    def montaTabelas_alunos(self):
        # Semore conectar ao banco de dados
        self.conecta_bd()
        # Criando tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name CHAR(40),
                    cell VARCHAR(11),
                    turma INTEGER(8) NOT NULL                          
            );
        """)
        print("=" * 113)
        print("=" * 113)
        self.conn.commit(); print("{:<45} BANCO DE DADOS CRIADO!".format(""))
        print("=" * 113)
        print("=" * 113)
        print("\033[1;30 \n       Aviso: 1- No caso do software não reconhecer o database, CERTIFIQUE-SE DE QUE O DATABASE ESTÁ NO MESMO DIRETÓRIO DA APLICAÇÃO  \033[m")
        print("\033[1;30 \n              2- O SOFTWARE PRECISA ESTÁ NO MESMO DIRETÓRIO DOS OUTROS ARQUIVOS QUE COMPOEM SUA EXECUÇÃO, PORTANTO NÃO FAÇA EXCLUSÃO E ALTERAÇÕES DENTRO DA PASTA\n \033[m")
        #Sempre desconectar com o banco de dados
        self.desconecta_bd()
        
        
        
        
    def montaTabelas_situation(self):
        # Semore conectar ao banco de dados
        self.conecta_bd()
        # Criando tabela      
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS aluno (
                    name CHAR(40) NOT NULL,
                    forma_de_pagamento NOT NULL,
                    mes NOT NULL,
                    pago NOT NULL

            );
        """)        #Qualquer coisa, foi erro de interpretação SQL
        
        self.conn.commit(); print("Banco de dados criado")
        #Sempre desconectar com o banco de dados
        self.desconecta_bd()
    
    def remove_duplicate(self):
        self.cursor.execute(""" DELETE FROM aluno WHERE rowid NOT IN (
                    SELECT MIN(rowid)
                    FROM aluno
                    GROUP BY name, forma_de_pagamento, mes);""")
        print("Identificando dados duplicados...")
        self.conn.commit()
       
    # OK
    def add_aluno(self):
        # importando as variáveis
        self.variable()
        if self.input_name.get() == "":
            print("\nAviso!! - Cadastro de cliente:\n")
            print("Para cadastrar um novo aluno, basta")
            print("que seja digitado pelo menos um nome")
            msg = "Para cadastrar um novo aluno, basta \n"
            msg += "que seja digitado pelo menos um nome"
            # CAIXA DE TEXTO
            messagebox.showinfo("Aviso!! - Cadastro de cliente", msg)
        else:
            self.conecta_bd()
            self.cursor.execute(""" INSERT INTO alunos (name, cell, turma)
                VALUES (?, ?, ?)""", (self.name, self.cell, self.turma,))
            self.conn.commit()
            self.desconecta_bd()
            self.conecta_bd()
            self.cursor.execute(""" DELETE FROM alunos WHERE rowid NOT IN (
                        SELECT MIN(rowid)
                        FROM alunos
                        GROUP BY name);""");print("Identificando dados duplicados...")
            self.conn.commit();print("\nNOVO CADASTRO:\n {}\n {}\n {}".format(self.name, self.cell, self.turma))
            # REMOVER DUPLICADOS
            self.select_lista2()
            self.desconecta_bd()

    # ANALISAR
    def add_situation_aluno(self):
        # importando as variáveis
        self.variable()
        
        # if self.
        if self.input_search_name.get() == "":
            print("\nNão foi possível conectar ao banco: requisição incompleta")
            msg = "Selecione um nome da tabela abaixo \n"
            # CAIXA DE TEXTO
            messagebox.showinfo("Aviso!! - Analise de aluno de cliente", msg)
        elif self.input_year.get() == "":
            print("\nNão foi possível conectar ao banco: requisição incompleta")
            msg = "Selecione o ano correspondente ao pagamento"
            # CAIXA DE TEXTO
            messagebox.showinfo("Aviso!! - Analise de aluno de cliente", msg)
        elif self.Tipvar3.get() == "Mês atual":
            print("\nNão foi possível conectar ao banco: requisição incompleta")
            msg = "Selecione o mês correspondente ao pagamento"
            # CAIXA DE TEXTO
            messagebox.showinfo("Aviso!! - Analise de aluno de cliente", msg)
        else:
            try:
                if self.name == "":
                    print("\nNão foi possível conectar ao banco: requisição incompleta")
                    msg = "Aluno não cadastrado!"
                    # CAIXA DE TEXTO
                    messagebox.showinfo("Aviso!! - Analise de aluno de cliente", msg)
                    self.Delete1()
                else:
                    self.variable()
                    self.conecta_bd()
                    
                    self.cursor.execute(""" UPDATE aluno SET pago = (?) WHERE mes = (?)""", (self.pago, self.data))# Por se tratar de uma tupla
                    self.conn.commit();print("Atualização...")
                    self.desconecta_bd()
                    self.select_lista1()
                    # self.Delete1()
                    
                    self.conecta_bd()#Referenciar qual aluno
                    self.cursor.execute(""" INSERT INTO aluno (name, forma_de_pagamento, mes, pago) 
                        VALUES (?, ?, ?, ?) """, (self.name, self.pay, self.data, self.pago))
                    self.conn.commit();print("\nPAGAMENTO ATUAL DO MÊS ONDE : \nAluno: {} \nValor: {} \nData: {}".format(self.name, self.pago, self.data))
                    self.remove_duplicate()
                    
                    self.desconecta_bd()
                    self.ativarState()
                    self.select_lista1()
                    # self.Delete1()
                    self.desativarState()
                    self.conecta_bd()
                    self.listaCli1.delete(*self.listaCli1.get_children())
                    # Tudo que tiver com o que eu digitei
                    self.input_search_name.insert(END, "%")
                    nome1 = self.input_search_name.get()
                    
                    # Like = procurar algo semelhante
                    self.cursor.execute(
                        """ SELECT name, forma_de_pagamento, mes, pago FROM aluno
                        WHERE name LIKE '%s' ORDER BY name ASC""" % nome1)
                    buscanomeCli1 = self.cursor.fetchall()
                    print("")
                    for i in buscanomeCli1:
                        self.listaCli1.insert("", END, values=i)
                        print(i)
                    print("")
                    self.desconecta_bd()
            except:
                print("\n \033[1;30BANCO BLOQUEADO! Reinicie o programa para poder reabrir o banco\033[m")
                msg = "Banco está bloqueado por segurança!"
                # CAIXA DE TEXTO
                messagebox.showinfo("Aviso!! - Analise de aluno de cliente", msg)
    # ANALISAR
    def select_lista1(self):
        self.listaCli1.delete(*self.listaCli1.get_children())
        self.conecta_bd()
        lista1 = self.cursor.execute(""" SELECT name, forma_de_pagamento, mes, pago FROM aluno
            ORDER BY name ASC; """)
        for i in lista1:
        # PECORRER O BANCO DE DADOS
            self.listaCli1.insert("", END, values=i)
        self.desconecta_bd()
    #OK 
    def select_lista2(self):
        self.listaCli2.delete(*self.listaCli2.get_children())
        self.conecta_bd()
        lista2 = self.cursor.execute(""" SELECT name, cell, turma FROM alunos
            ORDER BY name ASC; """)
        for i in lista2:
        # PECORRER O BANCO DE DADOS
            self.listaCli2.insert("", END, values=i)
        self.desconecta_bd()
        
    # ANALISAR   
    def busca_aluno1(self):
        self.conecta_bd()
        self.listaCli1.delete(*self.listaCli1.get_children())
        # Tudo que tiver com o que eu digitei
        self.input_search_name.insert(END, "%")
        nome1 = self.input_search_name.get()
        
        # Like = procurar algo semelhante
        self.cursor.execute(
            """ SELECT name, forma_de_pagamento, mes, pago FROM aluno
            WHERE name LIKE '%s' ORDER BY name ASC""" % nome1)
        buscanomeCli1 = self.cursor.fetchall()
        print("")
        for i in buscanomeCli1:
            self.listaCli1.insert("", END, values=i)
            print(i)
        print("")
        self.Delete1()
        self.desconecta_bd()

        
    # OK
    def busca_aluno2(self):
        self.conecta_bd()
        self.listaCli2.delete(*self.listaCli2.get_children())
        # Tudo que tiver com o que eu digitei
        self.input_name.insert(END, "%")
        nome2 = self.input_name.get()
        
        # Like = procurar algo semelhante
        self.cursor.execute(
            """ SELECT name, cell, turma FROM alunos
            WHERE name LIKE '%s' ORDER BY name ASC""" % nome2)
        buscanomeCli2 = self.cursor.fetchall()
        print("")
        for i in buscanomeCli2:
            self.listaCli2.insert("", END, values=i)
            print(i)
        print("")
        self.Delete2()
        self.desconecta_bd()
        
# Dois cliques OK
    def OnDoubleClick(self, event):
        self.ativarState()
        # importando função de deletar quando há 2click
        self.Delete1()
        # importando lista
        self.listaCli2.selection()
        for m in self.listaCli2.selection():
            col1 = self.listaCli2.item(m, 'values')
            self.input_search_name.insert(END, col1[0])
        self.desativarState()    
            
    # importando função de deletar quando há 2click
        self.Delete2()
        # importando lista
        self.listaCli2.selection()
        # dados a serem selecionados pelo 2 click
        for n in self.listaCli2.selection():
            col1, col2, col3 = self.listaCli2.item(n, 'values')
            self.input_name.insert(END, col1)
            self.input_cell.insert(END, col2)
    
    def OnDoubleClick2(self, event):
        self.ativarState()
        self.Delete1()
        self.listaCli1.selection()
        for m in self.listaCli1.selection():
            col1 = self.listaCli1.item(m, 'values')
            self.input_search_name.insert(END, col1[0])
        self.desativarState()         
# Excluir cliente
    def deleta_aluno1(self):
        # importando as variáveis
        self.variable()
        if self.input_search_name.get() == "":
            print("\nNão foi possível conectar ao banco: requisição incompleta")
            msg = "Selecione um nome da tabela abaixo \n"
            # CAIXA DE TEXTO
            messagebox.showinfo("Aviso!! - Analise de aluno de cliente", msg)    
        elif self.input_year.get() == "":
            print("\nNão foi possível conectar ao banco: requisição incompleta")
            msg = "Selecione o ano correspondente ao pagamento"
            # CAIXA DE TEXTO
            messagebox.showinfo("Aviso!! - Analise de aluno de cliente", msg)
        elif self.Tipvar3.get() == "Mês atual":
            print("\nNão foi possível conectar ao banco: requisição incompleta")
            msg = "Selecione o mês correspondente ao pagamento"
            # CAIXA DE TEXTO
            messagebox.showinfo("Aviso!! - Analise de aluno de cliente", msg)
        else: 
            self.conecta_bd()
            self.cursor.execute(""" DELETE FROM aluno WHERE name = ? AND mes = ? """, (self.search_name, self.data,))
            self.conn.commit();print("\nPagamento do mês cancelado:\nAluno: {} \nData: {}".format(self.search_name, self.data))
            self.desconecta_bd()
            # Limpar
            self.Delete1()
            # Atualizar
            self.select_lista1()
        
        
# Excluir cliente OK
    def deleta_aluno2(self):
        # importando as variáveis
        self.variable()
        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM alunos WHERE name = (?)""", (self.name,))
        self.conn.commit();print("\nCadastro deletado: {}".format(self.name))
        self.desconecta_bd()
        # Limpar
        self.Delete2()
        # Atualizar
        self.select_lista2()
        
# ANALISAR OK
    def altera_aluno2(self):
        self.variable()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE alunos SET name = (?), cell = (?), turma = (?)""", (self.name, self.cell, self.turma,))# Por se tratar de uma tupla
        self.conn.commit();print("\nCadastro Atualizado: \nAluno: {} \nCelular: {} \nTurma: {}".format(self.name, self.cell, self.turma))
        self.desconecta_bd()
        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM alunos WHERE rowid NOT IN (
                    SELECT MIN(rowid)
                    FROM alunos
                    GROUP BY name);""");print("Identificando dados duplicados...")
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista2()
        self.Delete2()
        
class Application(Function, GeneratePDF):
    def __init__(self):
        self.root = root
        self.tela_config()#Alterar para ingles
        self.Menus()
        self.frames()
        self.abas()
        self.widgets_1()
        self.widgets_2()
        self.widgets_3()
        self.montaTabelas_alunos()
        self.montaTabelas_situation()
        self.select_lista1()
        self.select_lista2()
        # self.windown()
        root.mainloop()
        
        
    def color(self):
        self.color_1 = "#107C41"#green
        self.color_2 = "#FFFFFF"#white
        self.color_3 = "#000000"#black
        
        
    def tela_config(self):
        self.color()
        self.root.title("Alunos do IESEM")

        self.root.configure(background=self.color_2)
        
        self.root.geometry("700x500")
        
        self.root.resizable(True, True)
        
        self.root.maxsize(width=900, height=700)
        
        self.root.minsize(width=500, height=400)
        
        self.root.state("zoomed")
        # iconic = aparece só na barra de tarefas
        
        # Alterar icone
        self.root.iconbitmap("Icone 1.ico")
        
    # def Menu(self):
        
    def frames(self):
        self.color()
        self.frame_1 = Frame(self.root, bd=2, bg=self.color_2, highlightbackground=self.color_1, highlightthickness=2)
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.47, relheight=0.46)
        
        self.frame_2 = Frame(self.root, bd=2, bg=self.color_2, highlightbackground=self.color_1, highlightthickness=2)
        self.frame_2.place(relx=0.51, rely=0.02, relwidth=0.47, relheight=0.46)
        
        self.frame_3 = Frame(self.root, bd=2, bg=self.color_2, highlightbackground=self.color_1, highlightthickness=2)
        self.frame_3.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight=0.46)
    def abas(self):
        self.color()
        # CRIANDO ABAS
        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)
        
        # DEFININDO BACKGROUND
        self.aba1.configure(background=self.color_2, bg=self.color_2)
        self.aba2.configure(background=self.color_2, bg=self.color_2)
        
        # ADICIONANDO TEXTO
        self.abas.add(self.aba1, text="Cadastro de Alunos")
        self.abas.add(self.aba2, text="Pagamento do mês")
        # POSIÇÃO DAS ABAS
        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    def button(self):
        self.color()
        # ABA 1
        self.bt_search = Button(self.aba1, text='Pesquisar', bd=2, bg = self.color_1, fg=self.color_2, font=('verdana', 8, 'bold'), command=self.busca_aluno2)
        self.bt_search.place(relx=0, rely=0.05, relwidth=0.2, relheight=0.15)
        
        self.bt_update = Button(self.aba1, text='Alterar', bd=2, bg = self.color_1, fg=self.color_2, font=('verdana', 8, 'bold'), command=self.altera_aluno2)
        self.bt_update.place(relx=0, rely=0.2, relwidth=0.2, relheight=0.15)
        
        self.bt_delete = Button(self.aba1, text='Deletar', bd=2, bg = self.color_1, fg=self.color_2, font=('verdana', 8, 'bold'), command=self.deleta_aluno2)
        self.bt_delete.place(relx=0, rely=0.35, relwidth=0.2, relheight=0.15)
        
        self.bt_sign = Button(self.aba1, text="Cadastrar", bd=2, bg = self.color_1, fg=self.color_2, font=('verdana', 8, 'bold'), command=self.add_aluno)         
        self.bt_sign.place(relx=0, rely=0.85, relwidth=0.2, relheight=0.15)
        
        
        
        # self.bt_clear = Button(self.aba1, text="Limpar", bd=2, bg = self.color_1, fg=self.color_2, font=('verdana', 8, 'bold')) 
        # self.bt_clear.place(relx=0, rely=0.85, relwidth=0.2, relheight=0.15)
        
        # ABA2
        
        self.bt_search2 = Button(self.aba2, text='Pesquisar', bd=2, bg = self.color_1, fg=self.color_2, font=('verdana', 8, 'bold'), command=self.busca_aluno1)
        self.bt_search2.place(relx=0.73, rely=0.10, relwidth=0.2, relheight=0.15)
        
        self.bt_pay = Button(self.aba2, text='Pago', bd=2, bg = self.color_1, fg=self.color_2, font=('verdana', 8, 'bold'), command=self.add_situation_aluno)
        self.bt_pay.place(relx=0.73, rely=0.6, relwidth=0.2, relheight=0.15)
        
        self.bt_delete_pay = Button(self.aba2, text='Deletar', bd=2, bg = self.color_1, fg=self.color_2, font=('verdana', 8, 'bold'), command=self.deleta_aluno1)
        self.bt_delete_pay.place(relx=0.73, rely=0.46, relwidth=0.2, relheight=0.15)
    def label(self):
        self.color()
        # ABA1
        self.lb_name = Label(self.aba1, text="Nome do Aluno", bg=self.color_2, fg=self.color_1)#cor do fundo do frame e do texto
        self.lb_name.place(relx= 0.30, rely=0.05)
        
        self.lb_cell = Label(self.aba1, text="Número de celular",  bg=self.color_2, fg=self.color_1)
        self.lb_cell.place(relx= 0.30, rely=0.3)
        
        self.lb_class = Label(self.aba1, text="Turma", bg=self.color_2, fg=self.color_1)
        self.lb_class.place(relx= 0.30, rely=0.60)
        
        # ABA2
        
        self.lb_name = Label(self.aba2, text="Nome do Aluno", bg=self.color_2, fg=self.color_1)#cor do fundo do frame e do texto
        self.lb_name.place(relx= 0.05, rely=0.05)
        
        self.lb_cell = Label(self.aba2, text="Forma de pagamento",  bg=self.color_2, fg=self.color_1)
        self.lb_cell.place(relx= 0.05, rely=0.3)
        
        self.lb_class = Label(self.aba2, text="Mês", bg=self.color_2, fg=self.color_1)
        self.lb_class.place(relx= 0.05, rely=0.55)
        
        self.lb_year = Label(self.aba2, text="Ano", bg=self.color_2, fg=self.color_1)
        self.lb_year.place(relx= 0.30, rely=0.55)
        
        self.lb_money = Label(self.aba2, text="Atualizar Saldo - R$", bg=self.color_2, fg=self.color_1)
        self.lb_money.place(relx= 0.05, rely=0.85)

    def Input(self):
        self.color()
        # ABA1
        self.input_name = Entry(self.aba1, bg=self.color_2, fg=self.color_3)
        self.input_name.place(relx= 0.30, rely=0.15, relwidth=0.6)
        
        self.input_cell = Entry(self.aba1, bg=self.color_2, fg=self.color_3)
        self.input_cell.place(relx= 0.30, rely=0.4, relwidth=0.4)
        
        self.Tipvar1 = StringVar(self.aba1)
        # Opções
        self.TipV1 = ("Básico", "Médio", "Bacharel")
        # Para aparecer em primeiro
        self.Tipvar1.set("Básico")
        self.popupMenu = OptionMenu(self.aba1, self.Tipvar1, *self.TipV1)
        self.popupMenu.place(relx = 0.30, rely=0.7, relwidth=0.2, relheight=0.1)
        self.Tipvar1.get()
        # print(self.turma)
        
        # ABA2

        self.input_search_name = Entry(self.aba2, bg=self.color_2, fg=self.color_3, state="readonly")
        self.input_search_name.place(relx= 0.05, rely=0.15, relwidth=0.6)
        
        self.Tipvar2 = StringVar(self.aba2)
        # Opções
        self.TipV2 = ("PIX", "Débito", "Crédito", "Dinheiro", "Cheque")
        # Para aparecer em primeiro
        self.Tipvar2.set("Dinheiro")
        self.popupMenu = OptionMenu(self.aba2, self.Tipvar2, *self.TipV2)
        self.popupMenu.place(relx = 0.05, rely=0.4, relwidth=0.2, relheight=0.1)

        
        self.Tipvar3 = StringVar(self.aba2)
        # Opções
        self.TipV3 = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
        # Para aparecer em primeiro
        self.Tipvar3.set("Janeiro")#Código para calendario
        self.popupMenu = OptionMenu(self.aba2, self.Tipvar3, *self.TipV3)
        self.popupMenu.place(relx = 0.05, rely=0.65, relwidth=0.2, relheight=0.1)
        # Mês
        # self.month = self.Tipvar.get()
        # print(self.turma)
        
        self.input_year = Entry(self.aba2, bg=self.color_2, fg=self.color_3, )
        self.input_year.place(relx= 0.3, rely=0.66, relwidth=0.15, relheight=0.08)

        self.input_money = Entry(self.aba2, bg=self.color_2, fg=self.color_3)
        self.input_money.place(relx= 0.33, rely=0.85, relwidth=0.15, relheight=0.08)
        
    def widgets_1(self):
        # ABA1 E ABA2
        self.button()
        self.label()
        self.Input()
            

    def widgets_2(self):
        
        self.lb_title = Label(self.frame_2, text="Situação dos alunos", bg=self.color_2, fg=self.color_1, font=("verdana", 20, "bold"))#cor do fundo do frame e do texto
        self.lb_title.place(relx= 0.15, rely=0.02)
        
        self.listaCli1 = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4", "col5"))
        
        self.listaCli1.heading("#0", text="")
        self.listaCli1.heading("#1", text="Nome")
        self.listaCli1.heading("#2", text="Pagamento")
        self.listaCli1.heading("#3", text="Mês")
        self.listaCli1.heading("#4", text="Valor")
        self.listaCli1.heading('#5', text="")
        
        self.listaCli1.column('#0', width=1)
        self.listaCli1.column("#1", width=100)
        self.listaCli1.column('#2', width=100)
        self.listaCli1.column('#3', width=100)
        self.listaCli1.column("#4", width=100)
        self.listaCli1.column('#5', width=1)
        
        self.listaCli1.place(relx=0.01, rely=0.15, relwidth=0.95, relheight=0.85)
        
    
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical', command=self.listaCli1.yview)

        self.listaCli1.configure(yscroll = self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        
        self.listaCli1.bind("<Double-1>", self.OnDoubleClick2)  
        
    def widgets_3(self):

        self.listaCli2 = ttk.Treeview(self.frame_3, height=3, column=("col1", "col2", "col3", "col4"))
        
        self.listaCli2.heading("#0", text="")
        self.listaCli2.heading("#1", text="Nome")
        self.listaCli2.heading("#2", text="Contato")
        self.listaCli2.heading("#3", text="Turma")
        self.listaCli2.heading("#4", text="")
        
        self.listaCli2.column('#0', width=1)
        self.listaCli2.column("#1", width=150)
        self.listaCli2.column('#2', width=125)
        self.listaCli2.column('#3', width=125)
        self.listaCli2.column('#4', width=1)

        
        self.listaCli2.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        
    
        self.scroolLista = Scrollbar(self.frame_3, orient='vertical', command=self.listaCli2.yview)

        self.listaCli2.configure(yscroll = self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        
        self.listaCli2.bind("<Double-1>", self.OnDoubleClick)  

        
        
    def Menus(self):
        # Variavel
        menubar = Menu(self.root)
        # Atribuindo variavel para configurar o menu
        self.root.config(menu=menubar)#Adicionando Menu
        
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        
        # Dentro do Menu
        def Quit(): self.root.destroy()#Fecha janela
        
        # Botão
        menubar.add_cascade(label= "Opções", menu = filemenu)
        menubar.add_cascade(label = "Relatórios", menu = filemenu2)
        # OPÇÕES
        filemenu.add_command(label="Sair", command= Quit)

        # Gerar PDF
        filemenu2.add_command(label = "Imprimir comprovante", command=self.generateReceipt)  
    # def windown(self):
        
        
Application()