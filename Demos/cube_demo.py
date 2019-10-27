from rhgl_transformations import *
from terminal_render import *
import time

rhgl_init()
rotateVal = 0.0
while True:
    rhgl_setFPS(60)
    verts = [[],[-0.5,-0.5,0.5],   #1
    [0.5, -0.5, 0.5],               #2
    [-0.5,0.5,0.5],                 #3
    [0.5,0.5,0.5],                  #4
    [-0.5,-0.5,-0.5],               #5
    [0.5, -0.5, -0.5],              #6
    [-0.5,0.5,-0.5],                #7
    [0.5,0.5,-0.5]]                 #8
    
    for x in range(1,len(verts)):
        verts[x] =rhgl_perspective(rhgl_translate((rhgl_rotateXZ(verts[x],rotateVal)),[1.0,1.0,1.0],[0.0,0.0,-1.5]),80.0, 3.0, 100.0)
    #First side
    rhgl_line(verts[1], verts[2])
    rhgl_line(verts[1], verts[3])
    rhgl_line(verts[2], verts[4])
    rhgl_line(verts[3], verts[4])
    

    #Second side
    rhgl_line(verts[5], verts[6])
    rhgl_line(verts[5], verts[7])
    rhgl_line(verts[8], verts[6])
    rhgl_line(verts[8],verts[7])
    
    # Remaining lines
    rhgl_line(verts[3], verts[7])
    rhgl_line(verts[4], verts[8])
    rhgl_line(verts[1],verts[5])
    rhgl_line(verts[2], verts[6])
 
    rhgl_swapBuffers()
    rotateVal += 0.05
