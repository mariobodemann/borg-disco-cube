from board import *
from neopixel import *
from time import *
from math import *
from random import *
from digitalio import *

p1=NeoPixel(A0, 10)
p2=NeoPixel(A1, 10)

p1.brightness = .5
p2.brightness = .5

p1.fill((0,0,0))
p2.fill((0,0,0))

green = list(map(lambda x: (0, randint(64, 255), 0), range(0,10)))
greenish = list(map(lambda x: (randint(0, 64), randint(16, 255), randint(0,64)), range(0,10)))
party = [
	(  0,  0,  0),
	(  0,  0,255),
	(  0,255,  0),
	(  0,255,255),
	(255,  0,  0),
	(255,  0,255),
	(255,255,  0),
	(255,255,255),
]

button = DigitalInOut(A2)
button.direction = Direction.INPUT

xs = [green, greenish, party]
xn = 0
x = xs[xn]

n=0
while True:
	if button.value:
		xn = (xn + 1) % len(xs)
		x = xs[xn]
		p1.fill((255,0,0))
		p2.fill((0,0,255))
		sleep(0.4)

	for i in range(0,10):
		l = len(x)	
		p1[i] = x[(n+i) % l]
		p2[i] = x[(n+(9-i)) % l]
		
	n+=1
	sleep(0.01)

	
