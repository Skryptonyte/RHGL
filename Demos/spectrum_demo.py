from rhgl_transformations import *
from terminal_render import *

rhgl_init()


while True:
    x = -1.0
    r,b,g = 255,0,0
    while (r >=0):
        rhgl_setRGB(r,g,b)
        rhgl_line([x,1.0],[x,-1.0])
        x += 2/768
        r -= 1; g += 1
    r,g,b = 0,255,0
    while g >=0:
        rhgl_setRGB(r,g,b)
        rhgl_line([x,1.0],[x,-1.0])
        x += 2/768
        g -= 1; b += 1
    r,g,b = 0,0,255
    while b >=0:
        rhgl_setRGB(r,g,b)
        rhgl_line([x,1.0],[x,-1.0])
        x += 2/768
        b -= 1; r += 1

    rhgl_swapBuffers()
