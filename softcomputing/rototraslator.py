#!/usr/bin/python

# import Scientific Pyhon Library and reference it as sp 
# import also numpy (numeric data type) library and reference it as np
import scipy as sp
import numpy as np

class geometric_transformation:

    actual_position = None

    def __init__(self, x, y, z):
        """ set initial position of the object """

        self.actual_position = np.array([x,y,z], np.int)

    def rotate_X_axis(self, degree):
        """ rotate the X axis with a rotation matrix multiplication 

            |1    0        0   |   | x |
            |0  cos(a)  -sin(a)| * | y |
            |0  sin(a)   cos(a)|   | z | 
        
        """ 

        #  radians to degree conversion 

        rotation_matrix_on_X_axis = np.matrix('1 0 0; 0 1 0; 0 0 1')

        self.actual_position = 
        


    def rotate_Y_axis(self, degree):

    def rotate_Y_axis(self, degree):

    def traslate(self, x,y,z):



        

def testunit():
    
    rt = rototraslator(10, 20, 30)
    rt.actual_position



__init__ = testunit()
