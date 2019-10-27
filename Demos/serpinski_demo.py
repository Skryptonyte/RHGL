from terminal_render import *
from rhgl_transformations import *



rhgl_init()
rhgl_syncFPS(10)
def serpinskiOrder(n,vertices):
    n -= 1;
    new_vertices = [[(vertices[0][0] + vertices[1][0])/2,(vertices[0][1] + vertices[1][1])/2, (vertices[0][2] + vertices[1][2])/2],
                    [(vertices[1][0] + vertices[2][0])/2,(vertices[1][1] + vertices[2][1])/2, (vertices[1][2] + vertices[2][2])/2],
                    [(vertices[2][0] + vertices[0][0])/2,(vertices[2][1] + vertices[0][1])/2, (vertices[2][2] + vertices[0][2])/2]]
    #rhgl_line(new_vertices[1],new_vertices[2])
    rhgl_triangle(new_vertices[0],new_vertices[1], new_vertices[2])
    if ( n > 0):
        serpinskiOrder(n, [new_vertices[0],new_vertices[1],vertices[1]])
        serpinskiOrder(n, [new_vertices[1],new_vertices[2],vertices[2]])
        serpinskiOrder(n, [new_vertices[0],new_vertices[2],vertices[0]])
while True:
    rhgl_triangle([0.0,1.0,0.0],[-1.0,-1.0,0.0],[1.0,-1.0,0.0])
    serpinskiOrder(3,[[0.0,1.0,0.0],[-1.0,-1.0,0.0],[1.0,-1.0,0.0]])
    rhgl_swapBuffers() 
