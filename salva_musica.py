import os
import sys
import platform


class MusicasSalvas:
    def __init__(self):
        self.user = os.getlogin()
        self.default_path = [fr'C:\Users\{self.user}\Downloads,', fr'C:\Users\{self.user}\Music']
        self.criar_ini()

    def criar_ini(self):
        if not (os.path.exists('playlist.PMlist')):
            with open('playlist.PMlist', 'w') as escrevendo:
                for index in self.default_path:
                    escrevendo.write(index)
                escrevendo.close()

    def lista_caminhos(self):
        with open('playlist.PMlist', 'r') as lendo_aquivo:
            lista_salva = lendo_aquivo.read().split(',')
        lendo_aquivo.close()
        if '' in lista_salva:
            lista_salva.remove('')
        return lista_salva

    def salvar_lista(self, diretorio: str):
        with open('playlist.PMlist', 'a') as escrevendo:
            escrevendo.write(',' + diretorio)
