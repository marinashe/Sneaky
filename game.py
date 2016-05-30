from random import random, randrange
from threading import Thread
from time import sleep
import RPi.GPIO as IO
from display import Display

button = 16
led = 15


def high(pin):
    IO.output(pin, IO.HIGH)


def low(pin):
    IO.output(pin, IO.LOW)


class Game(object):
    def __init__(self, display):
        self.counter = 0
        self.led = False
        self.display = display
        self.running = True
        IO.setup(button, IO.IN, pull_up_down=IO.PUD_UP)
        IO.setup(led, IO.OUT)

        def toggle_callback(channel):
            self.toggle()
            print('Toggle')

        IO.add_event_detect(button, IO.BOTH, toggle_callback, bouncetime=300)
        Thread(target=self.comp_start).start()

    def timer_plus(self):
        self.counter += 0.8

    def timer_minus(self):
        self.counter -= 1

    def toggle(self):
        self.led = not self.led
        if self.led:
            high(led)
            print('Led on')
        else:
            low(led)
            print('Led off')

    def start(self):
        print('Start game')
        try:
            while True:
                if self.led:
                    self.timer_minus()
                else:
                    self.timer_plus()
                self.display.set(int(self.counter))
                print(int(self.counter))
                sleep(0.2)
        except KeyboardInterrupt:
            self.comp_stop()
            self.display.stop()
            IO.cleanup()

    def comp_start(self):
        while self.running:
            sleep(randrange(1, 5))
            if not self.led:
                self.toggle()
                if random() > 0.8:
                    sleep(0.5)
                    self.toggle()

    def comp_stop(self):
        self.running = False



IO.setmode(IO.BOARD)
display = Display()
game = Game(display)
game.start()
