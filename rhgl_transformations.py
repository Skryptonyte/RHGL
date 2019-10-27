
import numpy as np
from math import *


def rhgl_translate(vertices,scaleList,offsetList):
    vector = np.array([[vertices[0]],[vertices[1]],[vertices[2]],[1.0]])
    translationMatrix = np.array([[scaleList[0],0.0,0.0,offsetList[0]],
                       [0.0,scaleList[1],0.0,offsetList[1]],
                       [0.0,0.0,scaleList[2],offsetList[2]],
                       [0.0,0.0,0.0,1.0]]
                        )
    result = translationMatrix.dot(vector).tolist()
    return [result[0][0]/result[3][0],result[1][0]/result[3][0],result[2][0]/result[3][0]]
    
def rhgl_rotateXY(vertices, radians):
    vector = np.array([[vertices[0]],[vertices[1]],[vertices[2]]])
    rotMatrix = np.array([[cos(radians), -sin(radians),0.0], 
                         [sin(radians), cos(radians),0.0],
                         [ 0.0, 0.0, 1.0]])
    result = rotMatrix.dot(vector).tolist()
    return [result[0][0],result[1][0],result[2][0],1.0]

def rhgl_rotateYZ(vertices, radians):
    vector = np.array([[vertices[0]],[vertices[1]],[vertices[2]]])
    rotMatrix = np.array([[1.0, 0.0,0.0],
                         [0.0 ,cos(radians),-sin(radians)],
                         [ 0.0, sin(radians), cos(radians)]])
    result = rotMatrix.dot(vector).tolist()
    return [result[0][0],result[1][0],result[2][0],1.0]

def rhgl_rotateXZ(vertices, radians):
    vector = np.array([[vertices[0]],[vertices[1]],[vertices[2]]])
    rotMatrix = np.array([[cos(radians), 0.0, -sin(radians)],
                          [0.0, 1.0, 0.0],
                         [sin(radians), 0.0, cos(radians)]])
    result = rotMatrix.dot(vector).tolist()
    return [result[0][0],result[1][0],result[2][0],1.0]


def rhgl_perspective(vertices, fov, near, far):
    vector = np.array([[vertices[0]],[vertices[1]],[vertices[2]],[1.0]])
    perspMatrix = np.array([[1/tan(fov/2),0.0,0.0,0.0],
                            [0.0, 1/tan(fov/2), 0.0, 0.0],
                            [0.0,0.0, -(near+far)/(far - near),-2*far*near/(far-near)],
                            [0.0, 0.0, -1.0, 0.0]])
    result = perspMatrix.dot(vector).tolist()
    return [result[0][0]/result[3][0],result[1][0]/result[3][0],result[2][0]/result[3][0]]


def rhgl_orthogonal(vertices, x, y, z):
    vector = np.array([[vertices[0]],[vertices[1]], [vertices[2]], [1.0]])
    xinter = x[1] - x[0]
    yinter = y[1] - y[0]
    zinter = z[1] - z[0]
    orthMatrix = np.array([ 2/xinter, 0.0, 0.0 , - (x[0] + x[1])/ xinter],
                          [ 0.0,2/yinter, 0.0, -(y[0] + y[1])/yinter],
                          [ 0.0, 0.0, -2 / zinter, -(z[0] + z[1])/zinter],
                          [ 0.0, 0.0, 0.0, 1.0])
    result = orthMatrix.dot(vector).tolist()
    return [result[0][0]/result[3][0],result[1][0]/result[3][0],result[2][0]/result[3][0]]


