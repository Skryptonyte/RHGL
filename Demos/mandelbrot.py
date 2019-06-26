from rhgl_transformations import *
from terminal_render import *
import terminal_render
rhgl_init()


dynamic_iters = 35
rhgl_init()
while 1:
    x = 0
    while x < x_range-1:
        y = 0
        while y < y_range-1:
            R = 0
            I = 0
            xn = ((2*x/x_range - 1 )); yn = 2*y/y_range - 1
            iters = dynamic_iters
            while (sqrt(R*R + I*I) <= 2.0 and iters >= 0):	
                RN = R*R - I*I
                IN = I*R
                IN += IN
                RN += xn
                IN += yn
                R,I = RN, IN
                #z = z*z + c
                rhgl_setRGB(iters * 5, 0, 0)
                rhgl_pixel(x,y)
                iters -= 1
            y += 1
        x += 1
    #dynamic_iters = (dynamic_iters + 1) % 31
    rhgl_swapBuffers()
            
