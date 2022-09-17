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

    def salva_lista_personalizada(self, diretorio_completo):
        '''
        suporte no máximo 5 playlist
        '''

        for count in range(1, 6):
            # nome do diretório
            nome_diretorio = diretorio_completo.split('/')[-1]
            # verificando se já existe pl anteriores
            if not os.path.exists(fr'{nome_diretorio[-1]}.MPVlist'):
                with open(f'{nome_diretorio}.MPVlist', 'w') as lista_personalizada:
                    lista_personalizada.write(',' + diretorio_completo)
                    return

    def procura_pl_personalizadas(self) -> list:
        lista = []
        for nome_arq in os.listdir('./'):
            if nome_arq.endswith('.MPVlist'):
                lista.append(fr'{nome_arq}')

        return lista
