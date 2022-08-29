from pynput import keyboard
import threading


class ListenerKeyboard:
    def __init__(self):
        super(ListenerKeyboard, self).__init__()


    def run(self):
        with keyboard.Listener() as listener:
            listener.join()
        return print(key)
