from rhgl_transformations import *
from terminal_render import *
import numpy as np

gravity = np.array([0,-2.5,0])

class generalObject:
    def __init__(self,position,mass=1):
        self.position = np.array(position)
        self.speed = np.array([0,0,0])
        self.acceleration = np.array(gravity)
              

        if mass == 0:
            self.inv_mass = 0
        else:
            self.inv_mass = 1/mass

class pointObject(generalObject):
    def resolveObject(self):
        rhgl_vertex((self.position).tolist())
    def resolvePhysics(self):
        speedToPosition = (self.speed)* rhgl_retrieveRegisters()[0]
        AccelerationToSpeed = self.acceleration * rhgl_retrieveRegisters()[0]

        self.position = self.position + speedToPosition
        self.speed = self.speed + AccelerationToSpeed

class boxObject(pointObject):
    def __init__(self, position, length, breadth, mass = 1):
        super().__init__(position, mass)
        self.length = np.array((length,0,0))
        self.breadth = np.array((0,breadth,0))
        
        self.norm = (np.array((1,0,0)), np.array((0,1,0)), np.array((-1,0,0)), np.array((0,-1,0)))


    def resolveObject(self):
        self.a = (self.position)
        self.b = (self.position + self.length)
        self.c = (self.position+self.length-self.breadth)
        self.d = (self.position-self.breadth)
        rhgl_quad(self.a.tolist(), 
                self.b.tolist(),
                self.c.tolist(),
                self.d.tolist())
def minmax(box1, box2):
    box1
    if (min1 < max2 or min2 < max1):
        return True
    else: 
        return False
def boxCollision(box1, box2):
    pass


def AABBCollision(box1,box2,normal):
    # Test X and Y axis
    xpass = lambda box1, box2: box1.c[0] > box2.d[0] and box2.c[0] > box1.d[0]
    ypass = lambda box1, box2: box1.a[1] > box2.c[1] and box2.a[1] > box1.c[1]

    xpenetration = min(box1.c[0] - box2.d[0], box2.c[0] - box2.d[0])
    ypenetration = min(box1.a[1] - box2.c[1], box2.a[1] - box1.c[1])
    if (xpass(box1, box2) or xpass(box2, box1)) and (ypass(box1, box2) or ypass(box2, box1)):
        a = np.dot(box1.norm[0], box2.norm[3])
        b = np.dot(box1.norm[1], box2.norm[2])
        c = np.dot(box1.norm[3], box2.norm[0])
        d = np.dot(box2.norm[2], box1.norm[1])

        rel = np.dot(box1.speed - box2.speed, normal)        
        if rel > 0:
            return       
        denom = box1.inv_mass + box2.inv_mass
        num = -(1 + 0.75)*rel
        impulse = num/denom
        box1.speed = box1.speed + box1.inv_mass * impulse * normal
        box2.speed = box2.speed - box2.inv_mass * impulse * normal
        #Do some gay collision shit
rhgl_init()
rhgl_syncFPS(30)
point = pointObject((0,0,0))
point.speed = np.array((0.5,0,0))

box = boxObject((-0.1,0.1,0),0.1,0.1)
box.speed = np.array((0.3,0,0))

barrier = boxObject((0.5,0.5,0.0),0.2, 0.5,10)

ground = boxObject((-0.9,-0.75,0.0),1.8,3.0,0.0)


while True:
    
    point.resolveObject()
    point.resolvePhysics()

    box.resolveObject()
    box.resolvePhysics()

    ground.resolveObject()
    
    barrier.resolveObject()
    barrier.resolvePhysics()
    AABBCollision(box,ground,np.array((0,1,0)))
    AABBCollision(barrier, ground,np.array((0,1,0)))
    AABBCollision(box, barrier,np.array((-1,0,0)))

    rhgl_swapBuffers()    
