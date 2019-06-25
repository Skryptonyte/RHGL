from terminal_render import *
import time
import math as m
rhgl_init()

phase = 0.0
while True:
    x = -1.0
    while (x <= 1.0):
        rhgl_vertex([x,1/2*sin(6*x + phase),0.0])
        x += 0.01
    time.sleep(0.01)
    phase += 0.05
    rhgl_swapBuffers()
