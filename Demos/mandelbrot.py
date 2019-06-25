from rhgl_transformations import *
from terminal_render import *

rhgl_init()


dynamic_iters = 1
while 1:
    x = -1.0
    while x <= 1.0:
        y = -1.0
        while y <= 1.0:
            c = complex(x,y)
            z = complex(0,0)
            iters = dynamic_iters
            while (abs(z) <= 2.0 and iters >= 0):
                colourCode = bin(iters).replace('0b','')[-3:]
                z = z*z + c
                rhgl_setRGB(0,0,iters*8)
                rhgl_vertex([x,y,0])
                iters -= 1
            y += 0.02
        x += 0.01
    dynamic_iters = (dynamic_iters + 1) % 31
    rhgl_swapBuffers()
            
