from random import choices
from string import digits, ascii_letters, punctuation
import PySimpleGUI as sg
import bancodedados


class TelaSenhas:
    def __init__(self):

        sg.theme('DarkBlack1')
        layout = [
            [sg.Output(size=(100, 15))],
            [sg.Button('Mostrar Serviços', size=(30, 1))],
            [sg.Button('Visualizar senha do usuario:', size=(30, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Button('Gerar senhas', size=(15, 1)),
             sg.Button('Menu', size=(15, 1)),
             sg.Button('Sair', size=(15, 1))]
        ]
        self.janela_senhas = sg.Window('Senhas', layout)

    def Iniciar(self):
        while True:
            evento, escolha = self.janela_senhas.read()
            if evento == 'Visualizar senha do usuario:':
                print('User/email, senha:')
                print(bancodedados.mostrar_senha(escolha['usuario']))
            elif evento == 'Mostrar Serviços':
                print('Sites cadastrados:')
                print(bancodedados.mostrar_sites())
            elif evento == 'Gerar senhas':
                self.janela_senhas.close()
                CriarSenha().Iniciar()
            elif evento == 'Menu':
                self.janela_senhas.close()
                Menu().Iniciar()
            else:
                break


class Menu:
    def __init__(self):

        sg.theme('DarkBlack1')
        layout = [
            [sg.Text('Menu: ', size=(10, 1))],
            [sg.Button('Gerar senhas', size=(15, 1))],
            [sg.Button('Visualizar senhas', size=(15, 1))],
            [sg.Button('Sair', size=(15, 1))]
        ]
        # Declarar janela
        self.janela_menu = sg.Window('Menu', layout)

    def Iniciar(self):
        while True:
            evento, opcao = self.janela_menu.read()
            if evento == 'Gerar senhas':
                self.janela_menu.close()
                CriarSenha().Iniciar()
            elif evento == 'Visualizar senhas':
                self.janela_menu.close()
                TelaSenhas().Iniciar()
            else:
                break


class TelaLogin:
    def __init__(self):
        self.senha_master = '123'
        sg.theme('DarkBlack1')
        layout = [
            [sg.Text('Senha de Autentição: ', size=(15, 1)),
             sg.Input(key='autenticacao', size=(20, 1))],
            [sg.Button('Confirmar', size=(15, 1))]
        ]
        # Declarar janela
        self.janela_login = sg.Window('Login', layout)

    def Iniciar(self):
        while True:
            evento, senha = self.janela_login.read()
            senha_master = self.senha_master
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Confirmar':
                if senha['autenticacao'] == senha_master:
                    self.janela_login.close()
                    Menu().Iniciar()
                else:
                    break


def gerar_senha(valores):
    chars_list = digits + ascii_letters + punctuation
    chars = choices(chars_list, k=int(valores['total_chars']))
    new_pass = ''.join(chars)
    return new_pass


class CriarSenha:
    def __init__(self):
        # Layout
        sg.theme('DarkBlack1')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/User', size=(10, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quant. de caracteres [1/30]'), sg.Combo(values=list(
                range(31)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 4))],
            [sg.Button('Gerar Senha', size=(15, 1)), sg.Button('Visualizar senhas', size=(15, 1))],
            [sg.Button('Menu', size=(15, 1)), sg.Button('Sair', size=(15, 1))]
        ]
        # Declarar janela
        self.janela = sg.Window('Gerador de senha', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == 'Gerar Senha':
                nova_senha = gerar_senha(valores)
                print('Senha: ', nova_senha)
                bancodedados.inserir_senha(valores['site'], valores['usuario'], nova_senha)
            elif evento == 'Menu':
                self.janela.close()
                Menu().Iniciar()
            elif evento == 'Visualizar senhas':
                self.janela.close()
                TelaSenhas().Iniciar()
            else:
                break


log = TelaLogin()
log.Iniciar()
bancodedados.close()
