import os
import sys
import platform


class ProcurarSalvasMusicas:
    def __init__(self):
        self.user = os.getlogin()
        self.default_path = [fr'C:\Users\{self.user}\Downloads,', fr'C:\Users\{self.user}\Music']
        self.criar_ini()

    def criar_ini(self):
        if not (os.path.exists('playlist.MPVlist')):
            with open('playlist.MPVlist', 'w') as escrevendo:
                for index in self.default_path:
                    escrevendo.write(index)
                escrevendo.close()

    def lista_caminhos(self, lista_padrao='playlist.MPVlist') -> list:
        with open(f'{lista_padrao}', 'r') as lendo_aquivo:
            lista_salva = lendo_aquivo.read().split(',')
        lendo_aquivo.close()
        if '' in lista_salva:
            lista_salva.remove('')
        return lista_salva

    def salvar_lista(self, diretorio: str):
        with open('playlist.MPVlist', 'a') as escrevendo:
            escrevendo.write(',' + diretorio)

    def salva_lista_personalizada(self, diretorio):
        '''
        suporte no máximo 5 playlist
        '''

        for count in range(1, 6):
            # verificando se já existe pl anteriores
            if not os.path.exists(f'{count} - playlist.MPVlist'):
                with open(f'{count} - playlist.MPVlist', 'w') as lista_personalizada:
                    lista_personalizada.write(',' + diretorio)
                    return

    def procura_pl_personalizadas(self) -> list:
        lista = []
        for count in range(1, 6):
            if os.path.exists(f'{count} - playlist.MPVlist'):
                lista.append(f'{count} - playlist.MPVlist')

        return lista
