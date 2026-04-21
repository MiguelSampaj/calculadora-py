from customtkinter import *
from rich.traceback import install
import re

# Visibilizando erros
install()

# Frames
# Frame das respostas
class FrameResposta(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=480, height=225)
        self.grid_propagate(False)

# Frame dos botões
class FrameButton(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=480, height=380, fg_color='transparent')
        self.grid_propagate(False)

# Classe do Botão
class Button(CTkButton):
    def __init__(self, master, name, **kwargs):
        super().__init__(master, **kwargs, width=114, height=70, font=CTkFont(family='Segoe UI', size=22), fg_color='#303030', hover_color='#292929')

        self.name = name

        # Configurando a imagem do botão
        self.configure(text=self.name)

# Main Root
class App(CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry('500x630')
        self.resizable(False, False)
        self.title('Calculadora')
        self.grid_propagate(False)

        # Cores
        but_red_color = '#ee1515'
        but_red_color_hover = '#be0000'
        but_equal_color = '#2153aa'
        but_equal_color_hover = '#124490'

        # Frame da resposta
        frame_resposta = FrameResposta(self)
        frame_resposta.grid(column=0, row=0, padx=10, pady=(10, 0))

        lbl_resposta = CTkLabel(frame_resposta,
                                text='0',
                                text_color='#fdfdff',
                                font=CTkFont(family='Segoe UI',
                                             size=27))
        lbl_resposta.grid(column=0, row=0, padx=15, pady=(84, 0))

        # Frame dos botões
        frame_button = FrameButton(self)
        frame_button.grid(column=0, row=1, padx=10, pady=10)

        # Função universal de funcionamento do botão
        def but_all_command(obj):
            name = obj.name
            oprs = ['+', '-', '*', '/', '/100', '.']
            texto = lbl_resposta.cget('text')

            if str(lbl_resposta.cget('text')) == '0' and name not in oprs:
                lbl_resposta.configure(text=name)
            elif len(str(lbl_resposta.cget('text'))) > 0:
                if (name != '*' and name!= '.' and texto[-1] not in oprs and texto[-1] != '(' and name in oprs) or name.isnumeric(): # Testando os números e os operadores exceto o '*' e o '.'
                    lbl_resposta.configure(text=str(texto) + name)

            if name == '*' and texto[-1] != '(': # Testando o '*'
                pattern_mult = re.compile(r'\*')
                match_mult = pattern_mult.finditer(str(texto))
                matchs_list = []

                if match_mult:
                    for match in match_mult:
                        matchs_list.append(int(match.start()))

                if len(matchs_list) > 1:
                    cond1 = (texto[-1] != '*' or int(matchs_list[-1]) - int(matchs_list[-2]) != 1) # Verificando se o último caractere é um '*' ou se tem dois '*' seguido
                    cond2 = texto[-1] not in oprs or texto[-1] == '*' # Verificando se o antecessor é um opr

                    if cond1 and cond2:
                        lbl_resposta.configure(text=texto + name)
                else:
                    if texto[-1] not in oprs or texto[-1] == '*':
                        lbl_resposta.configure(text=texto + name)

            if name == '.' and texto[-1] not in oprs and texto[-1] not in '()': # Testando o '.'
                pattern_dot = re.compile(r'[+\-*/]')
                list_doted = pattern_dot.split(texto)

                if list_doted[-1].count('.') == 0:
                    lbl_resposta.configure(text=texto + name)

            if name in '()': # Testando os parenteses
                if texto[-1] != '.':
                    lbl_resposta.configure(text=texto + name)

        # Botões
        # Coluna 0
        def but_apg_command():
            if len(str(lbl_resposta.cget('text'))) > 1:
                lbl_resposta.configure(text=str(lbl_resposta.cget('text'))[:-1])
            else:
                but_ce_command()

        but_apg = Button(frame_button, '<<<', command=but_apg_command)
        but_apg.configure(fg_color=but_red_color, hover_color=but_red_color_hover)
        but_apg.grid(column=0, row=0, padx=3, pady=3)

        but_sete = Button(frame_button, '7')
        but_sete.configure(command=lambda: but_all_command(but_sete))
        but_sete.grid(column=0, row=1, padx=3, pady=3)

        but_quatro = Button(frame_button, '4')
        but_quatro.configure(command=lambda: but_all_command(but_quatro))
        but_quatro.grid(column=0, row=2, padx=3, pady=3)

        but_um = Button(frame_button, '1')
        but_um.configure(command=lambda: but_all_command(but_um))
        but_um.grid(column=0, row=3, padx=3, pady=3)

        def but_ce_command():
            lbl_resposta.configure(text='0')

        but_ce = Button(frame_button, 'CE', command=but_ce_command)
        but_ce.configure(fg_color=but_red_color, hover_color=but_red_color_hover)
        but_ce.grid(column=0, row=4, padx=3, pady=3)

        # Coluna 1
        but_par_one = Button(frame_button, '(')
        but_par_one.configure(command=lambda: but_all_command(but_par_one))
        but_par_one.grid(column=1, row=0, padx=3, pady=3)

        but_oito = Button(frame_button, '8')
        but_oito.configure(command=lambda: but_all_command(but_oito))
        but_oito.grid(column=1, row=1, padx=3, pady=3)

        but_cinco = Button(frame_button, '5')
        but_cinco.configure(command=lambda: but_all_command(but_cinco))
        but_cinco.grid(column=1, row=2, padx=3, pady=3)

        but_dois = Button(frame_button, '2')
        but_dois.configure(command=lambda: but_all_command(but_dois))
        but_dois.grid(column=1, row=3, padx=3, pady=3)

        but_zero = Button(frame_button, '0')
        but_zero.configure(command=lambda: but_all_command(but_zero))
        but_zero.grid(column=1, row=4, padx=3, pady=3)

        # Coluna 2
        but_par_two = Button(frame_button, ')')
        but_par_two.configure(command=lambda: but_all_command(but_par_two))
        but_par_two.grid(column=2, row=0, padx=3, pady=3)

        but_nove = Button(frame_button, '9')
        but_nove.configure(command=lambda: but_all_command(but_nove))
        but_nove.grid(column=2, row=1, padx=3, pady=3)

        but_seis = Button(frame_button, '6')
        but_seis.configure(command=lambda: but_all_command(but_seis))
        but_seis.grid(column=2, row=2, padx=3, pady=3)

        but_tres = Button(frame_button, '3')
        but_tres.configure(command=lambda: but_all_command(but_tres))
        but_tres.grid(column=2, row=3, padx=3, pady=3)

        but_virgula = Button(frame_button, '.')
        but_virgula.configure(command=lambda: but_all_command(but_virgula))
        but_virgula.grid(column=2, row=4, padx=3, pady=3)

        # Coluna 3 (Coluna dos operadores)
        but_div = Button(frame_button, '/')
        but_div.configure(command=lambda: but_all_command(but_div))
        but_div.grid(column=3, row=0, padx=3, pady=3)

        but_mult = Button(frame_button, '*')
        but_mult.configure(command=lambda: but_all_command(but_mult))
        but_mult.grid(column=3, row=1, padx=3, pady=3)

        but_soma = Button(frame_button, '+')
        but_soma.configure(command=lambda: but_all_command(but_soma))
        but_soma.grid(column=3, row=2, padx=3, pady=3)

        but_sub = Button(frame_button, '-')
        but_sub.configure(font=CTkFont(family='Segoe UI', size=40), command=lambda: but_all_command(but_sub))
        but_sub.grid(column=3, row=3, padx=3, pady=3)

        def but_equal_command():
            try:
                resultado = eval(str(lbl_resposta.cget('text')))
                lbl_resposta.configure(text=str(resultado))
            except (SyntaxError, TypeError):
                lbl_erro = CTkLabel(frame_resposta,
                                    text='* Existe algum erro de sintaxe na sua operação',
                                    text_color=but_red_color,
                                    font=CTkFont(family='Segoe UI', size=20))
                lbl_erro.grid(column=0, row=1, padx=15, pady=55)
                lbl_resposta.configure(text='')
                lbl_erro.after(2500, lambda x=lbl_erro: x.destroy())
                lbl_resposta.after(2500, lambda x=lbl_resposta: x.configure(text='0'))

        but_equal = Button(frame_button, '=')
        but_equal.configure(fg_color=but_equal_color, hover_color=but_equal_color_hover, font=CTkFont(family='Segoe UI', size=30), command=but_equal_command)
        but_equal.grid(column=3, row=4, padx=0, pady=3)

app = App()
app.mainloop()
