import os
import time
from rhgl_transformations import *
x_range = 120
y_range = 60

display_buffer = []
rgb = [255,255,255]


deltatime = int(round(time.time() * 1000))
frametime_minima = 0
last_frametime = 0    # Useful for dynamically adjusting game speed based on frametimes
clearMode = ""


def rhgl_init():
    global display_buffer
    display_buffer = []
    for i in range(y_range):
        display_buffer.append([])
        for j in range(x_range):
            display_buffer[i].append(0)	

## Buffer Swap Modes

# At its core, rendering works solely on a double buffer system. The first buffer being the terminal's i.e the rendered image and the internal buffer of the library used for intermediate calculations before render

def rhgl_swapBuffers_fallback():
    global deltatime
    os.system(clearMode)
    for i in range(y_range-1,-1,-1):
        print('|',end='')
        for j in range(x_range):
            if (display_buffer[i][j]):
                print('\u2588',end='')
            else:
                print(' ',end='')
        print('|\n',end='')
    print("INFO: ",end='')
    deltatime = int(round(time.time() * 1000)) - deltatime
    if frametime_minima > deltatime:  
        d = frametime_minima - deltatime
        deltatime += d
        print("Frametime: ", deltatime, "ms",", Framerate: ",round(1000/deltatime)," FPS")
        time.sleep(d/1000)
    else:
        print("Frametime: ", deltatime, "ms",", Framerate: ",round(1000/deltatime)," FPS")
    deltatime = int(round(time.time() * 1000))
    rhgl_init()

def rhgl_swapBuffers_trueColor():
    global deltatime
    os.system(clearMode)
    for i in range(y_range-1,0,-1):
        print('|',end='')
        for j in range(x_range):
            if (display_buffer[i][j]):
                print('\033[38;2;{0};{1};{2}m'.format(display_buffer[i][j][0], display_buffer[i][j][1], display_buffer[i][j][2])+'\u2588'+'\033[0m',end='')
            else:
                print(' ',end='')
        print('|\n',end='')
    deltatime = int(round(time.time() * 1000)) - deltatime
    if frametime_minima > deltatime:
        d = frametime_minima - deltatime
        deltatime += d
        print("Frametime: ", deltatime, "ms",", Framerate: ",round(1000/deltatime)," FPS")
        time.sleep(d/1000)
    else:
        print("Frametime: ", deltatime, "ms",", Framerate: ",round(1000/deltatime)," FPS")
    deltatime = int(round(time.time() * 1000))
    rhgl_init()


## Initialize Library

bufferModes = {1: rhgl_swapBuffers_fallback, 2: rhgl_swapBuffers_trueColor}
rhgl_swapBuffers = rhgl_swapBuffers_trueColor

# Automatically set method of clearing buffer based on a simple OS check 

if os.name == 'nt':  # Mode for Windows platforms
    clearMode = "cls"
else:     # Mode for macOS, Linux, FreeBSD and other UNIX systems
    clearMode = "clear"

## Configurations

def rhgl_setRGB(r,g,b):
    global rgb
    rgb = [r,g,b]

def rhgl_setDrawMode(mode):
    global rhgl_swapBuffers 
    rhgl_swapBuffers = bufferModes[mode]

def rhgl_syncFPS(fps):    # Framelimiter can cause increased flickering
    global frametime_minima
    if fps == 0:    # Disable frame limiter
        mode = 0
    else:
        frametime_minima = round(int(1000/fps))

def rhgl_ClearMode(mode):
    global clearMode
    clearMode = mode
 
def rhgl_setDisplaySize(x,y):
    global x_range, y_range
    x_range = x
    y_range = y
    rhgl_init()
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

# Line Drawing using Bresenham's
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

