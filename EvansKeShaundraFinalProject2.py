import tkinter
import random
Width = 360
Height = 480
FPS = 30
#define colors
white =(255, 255, 255)
Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0, 255)
#initialize tkinter and create window
tkinter.init()
tkinter.mixer.init()
screen = tkinter.display.set_mode(Width,Height)
tkinter.display.set_caption("My Game")
clock = tkinter.time.Clock()
#loop
running = True
while running:
screen.fill(Blue)
