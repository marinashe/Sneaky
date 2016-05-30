# Sneaky

A game on RaspberryPi with a LED and a press button.

Your goal: To turn off the LED.
Each time you start pressing the button or release the button, the LED toggles (changes from ON to OFF or from OFF to ON).

The computer will turn the LED on randomally.  You will need to press or release the button to turn it off.
However, after a few seconds, as you are pressing (or not pressing) the button the computer will turn the LED on again, and you have to act again...

So - the comupter tries to keep the LED on while you try to keep it off...

Beware... Sometimes it will try to trick you to make you turn it on...

## Usage:
 * Single player (vs. RasPi):
 
 ```$ ./game.py single```
 
 * Two players: 
 
 ```$ ./game.py dual```
 

## The board
 ![alt tag](https://raw.githubusercontent.com/marinashe/Sneaky/master/media/board.jpg)
 
 You can check out some videos here: https://github.com/marinashe/Sneaky/blob/master/media
