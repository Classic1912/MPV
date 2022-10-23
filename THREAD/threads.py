# coding: utf-8
# author: V
from PySide6.QtCore import QThread
from pynput import keyboard
import time


class StatusMusica(QThread):
    def __init__(self, tela):
        super(StatusMusica, self).__init__()
        self.referencia = tela
        self.valor_anterior_horizontal_slider = 0

    def run(self):
        time.sleep(0.1)
        while True:

            # sempre setando para duração da música atualmente selecionada
            self.referencia.horizontalSlider.setMaximum(self.referencia.player.duration())

            # se foi anteriormente pausado o if é True
            if self.referencia.estado_play:
                # guardando o valor anterior, isso se da se o computador der um freeze o valor anterior é mantido
                anterior = self.valor_anterior_horizontal_slider
                self.referencia.horizontalSlider.setSliderPosition(anterior)
                self.referencia.player.setPosition(self.referencia.horizontalSlider.sliderPosition())
            # se não foi anteriormente pausado o if é False
            elif not self.referencia.estado_play:
                self.referencia.horizontalSlider.setSliderPosition(self.referencia.player.position())
                time.sleep(1)

                # diferencia é o resultado da diferença de segundos depois do freeze do thread
                diferenca = self.referencia.player.position() - self.referencia.horizontalSlider.sliderPosition()

                if diferenca > 1001 or diferenca < -1:
                    self.referencia.player.setPosition(self.referencia.horizontalSlider.sliderPosition())
                    time.sleep(0.1)


class Volume(QThread):
    def __init__(self, tela):
        super(Volume, self).__init__()
        self.referencia = tela

    def run(self):

        with keyboard.Listener(on_press=self.key_pressed) as listener:
            listener.join()

    def key_pressed(self, key):
        if key == keyboard.KeyCode(char='+'):
            self.referencia.player_output.setVolume(self.referencia.player_output.volume() + 0.005)

        if key == keyboard.KeyCode(char='-'):
            self.referencia.player_output.setVolume(self.referencia.player_output.volume() - 0.005)
