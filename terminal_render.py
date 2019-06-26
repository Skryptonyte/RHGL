import os
import time
from rhgl_transformations import *
x_range = 120
y_range = 60

display_buffer = []
rgb = [255,255,255]


deltatime = int(round(time.time() * 1000))
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
    global deltatime
    os.system("clear")
    for i in range(y_range-1,0,-1):
        print('|',end='')
        for j in range(x_range):
            if (display_buffer[i][j]):
                print('\033[38;2;{0};{1};{2}m'.format(display_buffer[i][j][0], display_buffer[i][j][1], display_buffer[i][j][2])+'\u2588'+'\033[0m',end='')
            else:
                print(' ',end='')
        print('|\n',end='')
    deltatime = int(round(time.time() * 1000)) - deltatime
    print("Frametime: ", deltatime, "ms",", Framerate: ",round(1000/deltatime)," FPS")
    deltatime = int(round(time.time() * 1000))
    rhgl_init()


## Initialize Library

rhgl_swapBuffers = rhgl_swapBuffers_trueColor

# Configurations

def rhgl_setRGB(r,g,b):
    global rgb
    rgb = [r,g,b]
# Drawing

def rhgl_pixel(x, y):
    display_buffer[y][x] = rgb
def rhgl_vertex(vectorCoords: list):
    global x_range, y_range
    x = abs((vectorCoords[0] + 1)/2); y = abs((vectorCoords[1] + 1)/2); z = abs((vectorCoords[1]+1)/2);
    try:
        display_buffer[int(y * (y_range - 1))][int(x*(x_range - 1))] = [rgb[0], rgb[1], rgb[2]]
    except:
        pass


def rhgl_line(vert1: list, vert2: list):
    x1 = int((vert1[0]+1)/2 * (x_range-1)); x2 = int((vert2[0]+1)/2 * (x_range-1));
    y1 = int((vert1[1]+1)/2 * (y_range-1)); y2 = int((vert2[1]+1)/2 * (y_range-1));
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
            display_buffer[y][x] = [rgb[0], rgb[1], rgb[2]]
            if ((error + yinc*dy)<<1 < xinc* dx):
                error += dy * yinc
            else:
                error += yinc*dy - xinc*dx
                y += yinc
    elif(abs(dy) > abs(dx)):
        x = x1
        error = yinc *(dx >> 1)
        for y in range(y1, y2,yinc):
            display_buffer[y][x] = [rgb[0], rgb[1], rgb[2]]
            if ((error + xinc*dx)<<1 < yinc*dy):
                error += dx*xinc
            else:
                error += xinc* dx - yinc*dy
                x += xinc
    
def rhgl_triangle(a, b, c):
    rhgl_line(a,b)
    rhgl_line(b, c)
    rhgl_line(a,c)

