import os
import sys
import platform


class MusicasSalvas:
    def __init__(self):
        self.user = os.getlogin()
        self.default_path = [fr'C:\Users\{self.user}\Downloads,', fr'C:\Users\{self.user}\Music']
        self.criar_ini()

    def criar_ini(self):
        if not (os.path.exists('teste.ini')):
            with open('teste.ini', 'w') as escrevendo:
                for index in self.default_path:
                    escrevendo.write(index)
                escrevendo.close()

    def lista_caminhos(self):
        with open('teste.ini', 'r') as lendo_aquivo:
            lista_salva = lendo_aquivo.read().split(',')
        lendo_aquivo.close()
        if '' in lista_salva:
            lista_salva.remove('')
        return lista_salva

    def salvar_lista(self, diretorio: str):
        with open('teste.ini', 'a') as escrevendo:
            escrevendo.write(',' + diretorio)
