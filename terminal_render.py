import os
import time
from rhgl_transformations import *
x_range = 160
y_range = 60

display_buffer = []
rgb = [255,255,255]


def rhgl_init():
    global display_buffer
    display_buffer = []
    for i in range(y_range):
        display_buffer.append([])
        for j in range(x_range):
            display_buffer[i].append(0)	

def rhgl_swapBuffers_fallback():
    os.system("clear")
    for i in range(y_range-1,0,-1):
        print('|',end='')
        for j in range(x_range):
            if (display_buffer[i][j]):
                print('\u2588',end='')
            else:
                print(' ',end='')
        print('|\n',end='')
    rhgl_init()

def rhgl_swapBuffers_trueColor():
    os.system("clear")
    for i in range(y_range-1,0,-1):
        print('|',end='')
        for j in range(x_range):
            if (display_buffer[i][j]):
                print('\033[38;2;{0};{1};{2}m'.format(display_buffer[i][j][0], display_buffer[i][j][1], display_buffer[i][j][2])+'\u2588'+'\033[0m',end='')
            else:
                print(' ',end='')
        print('|\n',end='')
    rhgl_init()


## Initialize Library

rhgl_swapBuffers = rhgl_swapBuffers_trueColor

# Configurations

def rhgl_setRGB(r,g,b):
    global rgb
    rgb = [r,g,b]
# Drawing

def rhgl_vertex(vectorCoords: list):
    global x_range, y_range
    x = abs((vectorCoords[0] + 1)/2); y = abs((vectorCoords[1] + 1)/2); z = abs((vectorCoords[1]+1)/2);
    try:
        display_buffer[int(y * (y_range - 1))][int(x*(x_range - 1))] = [rgb[0], rgb[1], rgb[2]]
    except:
        pass



def rhgl_line_naive(vert1: list, vert2: list):
    global x_range, y_range
    if (vert1[0] * (x_range-1) == vert2[0] * (x_range-1)):
        i = max(vert1[1], vert2[1])
        while (i >= min(vert1[1],vert2[1])):
            rhgl_vertex([vert1[0],i,0.0])
            i -= 0.001
        return
    slope = (vert1[1] - vert2[1]) / (vert1[0] - vert2[0])

    if (int(vert1[1] * (y_range-1)) == int(vert2[1] * (y_range-1))): 
        i = max(vert1[0], vert2[0])
        while (i >= min(vert1[0],vert2[0])):
            rhgl_vertex([i,vert1[1],0.0])
            i -= 0.001
        return
    c = vert1[1] - vert1[0] * slope
    c2 = vert2[1] - vert2[0] * slope
    #print("Constant: ",c, c2,"Slope: ",slope)

    i = max(vert1[1],vert2[1])
    while i >= min(vert1[1], vert2[1]):
        rhgl_vertex([(i - c)/slope,i,0.0])
        i -= 0.001

def rhgl_line_bresenham(vert1: list, vert2: list):
    for i in range(2):
        vert1[i] = abs((vert1[i] + 1) / 2)
        vert2[i] = abs((vert2[i] + 1) / 2)
    x1 = int(vert1[0] * (x_range-1)); x2 = int(vert2[0] * (x_range-1));
    y1 = int(vert1[1] * (y_range-1)); y2 = int(vert2[1] * (y_range-1));
    dy = y2 - y1
    dx = x2 - x1
    xinc = 0; yinc = 0
    if (x1 <= x2):
         xinc = 1
    else:
        xinc = -1
    if (y1 <= y2):
        yinc = 1
    else:
        yinc = -1
    if ( abs(dx) >= abs(dy)):
        error = yinc*(dy >> 1)
        y = y1
        for x in range(x1,x2,xinc):
            display_buffer[y][x] = 1
            if ((error + yinc*dy)<<1 < xinc* dx):
                error += dy * yinc
            else:
                error += yinc*dy - xinc*dx
                y += yinc
    elif(abs(dy) > abs(dx)):
        x = x1
        error = yinc *(dx >> 1)
        for y in range(y1, y2,yinc):
            display_buffer[y][x] = 1
            if ((error + xinc*dx)<<1 < yinc*dy):
                error += dx*xinc
            else:
                error += xinc* dx - yinc*dy
                x += xinc


default_line = rhgl_line_naive
def rhgl_line(vert1,vert2):
    default_line(vert1, vert2)         
    
def rhgl_triangle(a, b, c):
    rhgl_line(a,b)
    rhgl_line(b, c)
    rhgl_line(a,c)

"""
le = 0.0
while True:
    rhgl_init()
    #rhgl_line(rhgl_rotateXY([-0.5,-0.5,0.0],le),(rhgl_rotateXY([0.5,-0.5,0.0],le)))
    #rhgl_line(rhgl_rotateXY([-0.5,-0.5,0.0],le),(rhgl_rotateXY([0.0,0.5,0.0],le)))
    #rhgl_line(rhgl_rotateXY([0.5,-0.5,0.0],le),(rhgl_rotateXY([0.0,0.5,0.0],le)))
    rhgl_triangle(rhgl_rotateXY([-0.5,-0.5,0.5],le), rhgl_rotateXY([0.5,-0.5,0.0],le), rhgl_rotateXY([0.0,0.5,0.0], le))
    rhgl_vertex([0.0,0.0,0.0])
    #rhgl_vertex2f(rhgl_rotate([0.5,0.0],le)[0],rhgl_rotate([0.5,0.0],le)[1])
    rhgl_swapBuffers()
    le += 0.1
"""
