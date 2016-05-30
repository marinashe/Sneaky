from threading import Thread
from time import sleep
import RPi.GPIO as IO
from display import Display

button = 16
led = 19


def high(pin):
    IO.output(pin, IO.HIGH)


def low(pin):
    IO.output(pin, IO.LOW)


class Game(object):
    def __init__(self, display):
        self.counter = 0
        self.led = False
        self.display = display
        IO.setup(button, IO.IN, pull_up_down=IO.PUD_UP)
        IO.setup(led, IO.OUT)

        def toggle_callback(channel):
            self.toggle()

        IO.add_event_detect(button, IO.BOTH, toggle_callback, bouncetime=1000)

    def timer_plus(self):
        self.counter += 0.03

    def timer_minus(self):
        self.counter -= 0.03

    def toggle(self):
        self.led = not self.led
        if self.led:
            high(led)
        else:
            low(led)

    def start(self):
        try:
            while True:
                if self.led:
                    self.timer_minus()
                else:
                    self.timer_plus()
                self.display.set(int(self.counter))
                sleep(0.2)
        except KeyboardInterrupt:
            IO.cleanup()


IO.setmode(IO.BOARD)
display = Display()
game = Game(display)
game.start()
