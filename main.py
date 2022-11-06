# coding: utf-8
# author: V
import os
import sys
import time

from THREAD import threads
import salva_musica
import mod_stylesheet

from PySide6.QtCore import QUrl, QPoint, Qt
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from JanelaMPV import Ui_MusicPlayer


class LogicaApp(QMainWindow, Ui_MusicPlayer):
    def __init__(self):
        super(LogicaApp, self).__init__()
        # Variáveis utilizadas posteriormente
        self.nome_pl_personalizadas = None
        self.evento_antigo = None
        self.evento = None
        self.dicionario = {}
        self.nome_musica = []
        self.caminhos_completo = []
        self.estado_play = bool
        self.estado_pausado_anterior = False

        # configurações iniciais
        self.player = QMediaPlayer()
        self.player_output = QAudioOutput()

        # thread que escuta o teclado
        self.keys = threads.Volume(self)
        # thread geral de funções do PM
        self.status_musica = threads.StatusMusica(self)

        self.lista_caminhos = salva_musica.ProcurarSalvasMusicas()
        self.player_output.setVolume(1.0)
        self.instancia_janela = Ui_MusicPlayer()
        self.setupUi(self)

        # desativando a 'moldura' da janela
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.bt_anterior.clicked.connect(self.anterior)
        self.bt_play.clicked.connect(self.play)
        self.bt_proximo.clicked.connect(self.next)
        self.bt_diretorio.clicked.connect(self.salvar_caminhos)
        self.bt_sair.clicked.connect(self.sair_app)
        self.bt_minimizar.clicked.connect(lambda: self.showMinimized())
        self.listWidget.clicked.connect(self.doble_click_musica)
        self.bt_salva_pl_personalizada.clicked.connect(self.salva_caminhos_pl_personalizada)
        self.cb_lista_playlist.currentTextChanged.connect(self.procurar_musicas)
        self.player.playbackStateChanged.connect(self.ultima_musica)
        self.listWidget.setMovement(self.listWidget.Movement.Free)
        self.listWidget.setDefaultDropAction(Qt.MoveAction)
        self.procurar_musicas()

    def ultima_musica(self):
        if self.player.mediaStatus() == self.player.EndOfMedia:
            self.next()

    def sair_app(self):
        self.destruir_thread()
        self.close()

    # se for fechado por motivo não pensado
    def closeEvent(self, event):
        self.sair_app()

    # capturando o evento do mouse para mover a tela
    def mousePressEvent(self, event):
        self.evento_antigo = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        # se o mouse for pressionado e movido sobe um botão é levantado uma exceção
        try:
            delta = QPoint(event.globalPosition().toPoint() - self.evento_antigo)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.evento_antigo = event.globalPosition().toPoint()

        except TypeError:
            pass

    def reset_config_bar(self):
        self.horizontalSlider.setPageStep(0)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setMaximum(self.player.duration())

    # Procura arquivos com extensão '.mp3' no diretório especificado
    def procurar_musicas(self):

        # reset tudo para não ter duplicação
        self.listWidget.clear()
        self.dicionario = {}
        self.nome_musica = []
        self.caminhos_completo = []

        self.nome_pl_personalizadas = \
            self.lista_caminhos.procura_pl_personalizadas()
        # se for maior que 0 existe uma pl personalizada
        if len(self.nome_pl_personalizadas) > 0:
            for nome in self.nome_pl_personalizadas:
                # se o nome não existir é adicionado no ComboBox 
                if self.cb_lista_playlist.findText(nome) == -1:
                    self.cb_lista_playlist.addItem(f'{nome}')

        # Se o diretório for inválido é levantado uma exceção
        try:
            for directory in self.lista_caminhos.lista_caminhos(self.cb_lista_playlist.currentText()):
                for arquivo in os.listdir(directory):
                    if arquivo.endswith('.mp3'):
                        # Guardando o nome da música
                        self.nome_musica.insert(-1, arquivo)

                        self.caminhos_completo.insert(0, os.path.join(directory, arquivo))
                        self.dicionario.update({arquivo: self.caminhos_completo[0]})

            self.nome_musica.sort()
            indices = 0
            for _ in self.caminhos_completo:
                self.listWidget.addItem(self.nome_musica[indices])
                indices += 1

        except FileNotFoundError:
            pass

    # salva pl personalizada
    def salva_caminhos_pl_personalizada(self):
        caminho_selecionado = QFileDialog.getExistingDirectory(self)
        if len(caminho_selecionado) != 0:
            # se o retorno de a for igual a uma ‘string’ vazia o valor é zero
            self.lista_caminhos.salva_lista_personalizada(caminho_selecionado)
            self.procurar_musicas()

    # salva o caminho das músicas selecionada pelo usuário
    def salvar_caminhos(self):
        caminho_selecionado = QFileDialog.getExistingDirectory(self)
        # se o retorno de a for igual a uma ‘string’ vazia o valor é zero
        if len(caminho_selecionado) != 0:
            self.lista_caminhos.salvar_lista(caminho_selecionado)
            self.procurar_musicas()

    # verifica se a Thread esta viva e a destrói
    def destruir_thread(self):
        if self.keys.isRunning():
            self.keys.terminate()
            self.keys.isRunning()
        if self.status_musica.isRunning():
            self.status_musica.terminate()
            self.status_musica.isRunning()

    # Reproduzir a música selecionada
    def doble_click_musica(self):
        self.player.stop()
        self.player.setSource(
            QUrl.fromLocalFile(f'{self.dicionario.get(self.listWidget.currentItem().text())}'))
        self.estado_play = True
        self.reset_config_bar()
        self.play()

    def anterior(self):
        self.keys.terminate()
        self.player.stop()
        # se for a primeira música a anterior sera ela mesma
        if self.listWidget.currentRow() == 0:
            self.listWidget.setCurrentRow(0)

        else:
            self.listWidget.setCurrentRow(self.listWidget.currentRow() - 1)

        self.player.setSource(
            QUrl.fromLocalFile(f'{self.dicionario.get(self.listWidget.item(self.listWidget.currentRow()).text())}'))

        # colocando o play para tocar a música
        self.estado_play = True
        self.reset_config_bar()
        self.play()

    def next(self):
        self.keys.terminate()
        self.player.stop()

        # retornando o curso de reprodução para o início
        if self.listWidget.currentRow() == (len(self.caminhos_completo) - 1):
            self.listWidget.setCurrentRow(0)
        else:
            self.listWidget.setCurrentRow(self.listWidget.currentRow() + 1)

        self.player.setSource(
            QUrl.fromLocalFile(f'{self.dicionario.get(self.listWidget.item(self.listWidget.currentRow()).text())}'))

        # colocando o play para tocar a música
        self.estado_play = True
        self.reset_config_bar()
        self.play()

    def play(self):
        # se True o player esta no estado de Play
        if self.estado_play:
            # se -1 não tem nenhuma música
            if self.listWidget.currentRow() == -1:
                self.l_selec_pasta.setVisible(True)
                self.procurar_musicas()
                # selecionando a primeira música
                self.listWidget.setCurrentRow(0)

            else:
                self.l_selec_pasta.setVisible(False)
                self.l_selec_pasta_personalizada.setVisible(False)

                # caso seja a primeira música a tocar o if é executado
                if not self.estado_pausado_anterior:
                    url = QUrl.fromLocalFile(
                        f'{self.dicionario.get(self.listWidget.item(self.listWidget.currentRow()).text())}')
                    self.player.setAudioOutput(self.player_output)
                    self.player.setSource(url)
                    self.reset_config_bar()

                self.keys.start()
                self.status_musica.start()
                self.player.play()
                self.estado_play = False
                # alterando o icon para icon de pause
                self.bt_play.setStyleSheet(mod_stylesheet.bt_play_pause)

        # se False o player esta no estado de Pause
        else:
            self.player.pause()

            # alterando o icon para icon de play
            self.bt_play.setStyleSheet(mod_stylesheet.bt_play)
            self.estado_play = True

            # se a música foi pausada o valor e True
            self.estado_pausado_anterior = True
            self.status_musica.valor_anterior_horizontal_slider = self.player.position()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = LogicaApp()
    janela.show()
    sys.exit(app.exec())
