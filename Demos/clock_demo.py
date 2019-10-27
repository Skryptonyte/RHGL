from rhgl_transformations import *
from terminal_render import *
import time

secs = 0
mins = 0
rhgl_init()
while True:
    r = 0.0
    rhgl_vertex([0.9,0.9,0.0])
    rhgl_vertex([0.75,0.25,0.0])
    while r < 3.1415 * 2:
        #print(rhgl_rotateXY([0.0,0.5,0.0],r))
        rhgl_vertex([0.0,0.0,0.0])
        rhgl_vertex(rhgl_rotateXY([0.0,0.5,0.0],r))
        r += 0.01
    rhgl_line([0.0,0.0,0.0],rhgl_rotateXY([0.0,0.5,0.0],secs*(-3.14 / 30)))
    rhgl_line([0.0,0.0,0.0],rhgl_rotateXY([0.0,0.35,0.0],mins*(-3.14 / 30)))
    rhgl_swapBuffers()
    if (secs == 59):
        mins = (mins + 1) % 60
    secs = (secs + 1) % 60
