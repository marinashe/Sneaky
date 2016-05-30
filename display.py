from threading import Thread
from time import sleep
import RPi.GPIO as IO

positions = {
    1: 3,
    2: 5,
    3: 7,
    4: 11,
    }

segments = {
    'a': 12,
    'b': 18,
    'c': 26,
    'd': 24,
    'e': 22,
    'f': 13,
    'g': 19,
    }

chars = {
    '1': 'bc',
    '2': 'abged',
    '3': 'abcdg',
    '4': 'fgbc',
    '5': 'afgcd',
    '6': 'fedcg',
    '7': 'abc',
    '8': 'abcdefg',
    '9': 'abcdfg',
    '0': 'abcdef',
    'a': 'efgabc',
    'b': 'fegcd',
    'c': 'afed',
    'd': 'bcdeg',
    'e': 'afged',
    'f': 'afge',
    'g': 'afgedc',
    'h': 'febcg',
    'i': 'bc',
    'j': 'bcd',
    'l': 'fed',
    'o': 'abcdef',
    'p': 'fabge',
    's': 'afgcd',
    'u': 'fedcb',
    '-': 'g',
    ' ': '',
    }


def high(pin):
    IO.output(pin, IO.HIGH)


def low(pin):
    IO.output(pin, IO.LOW)


def clear_segments():
    for seg in segments.values():
        low(seg)


def char_on(char):
    for seg in chars[char]:
        high(segments[seg])


def position_on(led):
    low(positions[led])


def position_off(led):
    high(positions[led])


class Display(object):
    def __init__(self):
        self.value = '0'
        self.running = True
        for pin in positions.values() + segments.values():
            IO.setup(pin, IO.OUT)
        for pin in positions.values():
            high(pin)
        Thread(target=self.start).start()

    def start(self):
        while self.running:
            for i, c in enumerate(self.value, 1):
                char_on(c)
                position_on(i)
                sleep(0.002)
                position_off(i)
                clear_segments()

    def set(self, x):
        if len(str(x)) > 4:
            raise ValueError('Invalid value for display: {}'.format(x))
        self.value = str(x).rjust(4, ' ')

    def stop(self):
        self.running = False




