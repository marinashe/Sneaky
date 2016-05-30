import sys
from random import random, randrange
from threading import Thread
from time import sleep
import RPi.GPIO as IO
from display import Display

button1 = 16
button2 = 21
led = 15


def high(pin):
    IO.output(pin, IO.HIGH)


def low(pin):
    IO.output(pin, IO.LOW)


class Game(object):
    def __init__(self, display, type_game):
        self.counter = 0
        self.led = False
        self.display = display
        self.running = True
        IO.setup(button1, IO.IN, pull_up_down=IO.PUD_UP)
        IO.setup(button2, IO.IN, pull_up_down=IO.PUD_UP)
        IO.setup(led, IO.OUT)
        low(led)

        def toggle_callback(channel):
            self.toggle()
            print('Toggle')

        IO.add_event_detect(button1, IO.BOTH, toggle_callback, bouncetime=100)
        IO.add_event_detect(button2, IO.BOTH, toggle_callback, bouncetime=100)
        if type_game == 'single':
            Thread(target=self.comp_start).start()

    def timer_plus(self):
        self.counter += 1

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

        while True:
            if self.led:
                self.timer_minus()
            else:
                self.timer_plus()
            self.display.set(int(self.counter))
            print(int(self.counter))
            sleep(0.2)

    def comp_start(self):
        while self.running:
            sleep(randrange(1, 5))
            if not self.led:
                self.toggle()
                if random() > 0.8:
                    sleep(0.5)
                    self.toggle()

    def stop(self):
        self.running = False
        self.display.stop()
        sleep(0.5)
        IO.cleanup()


if __name__ == '__main__':
    IO.setmode(IO.BOARD)
    display = Display()
    game = Game(display, sys.argv[1])
    try:
        game.start()
    except KeyboardInterrupt:
        game.stop()
