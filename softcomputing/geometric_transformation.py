#!/usr/bin/python

# import Scientific Pyhon Library and reference it as sp 
import scipy as sp

# import also numpy (numeric data type) library and reference it as np
import numpy as np

class geometric_transformation:

    actual_position = None

    def __init__(self, x, y, z):
        """ set initial position of the object """

        self.actual_position = np.array([[x],[y],[z]])

    def rotate_X_axis(self, radians):
        """ rotate the X axis with a rotation matrix multiplication 

            |1    0        0   |   | x |
            |0  cos(a)  -sin(a)| * | y |
            |0  sin(a)   cos(a)|   | z | 
        
        """ 

        # rotation matrix creation 
        a,b,c = 1, 0, 0 
        d,e,f = 0, np.cos(radians), -np.sin(radians)
        g,h,i = 0, np.sin(radians), +np.cos(radians)

        rotation_matrix_on_X_axis = np.array([[a,b,c],[d,e,f],[g,h,i]])

        # perform rotation 
        self.actual_position = np.dot(rotation_matrix_on_X_axis , self.actual_position)

        return self.actual_position

    def rotate_Y_axis(self, radians):
        """ rotate the Y axis with a rotation matrix multiplication 

            |cos(b)     0       sin(b)|   | x |
            |   0       1         0   | * | y |
            |-sin(b)    0       cos(b)|   | z | 
        
        """ 

        # rotation matrix creation 
        a,b,c = np.cos(radians),  0, np.sin(radians)
        d,e,f = 0,1,0
        g,h,i = -np.sin(radians), 0, np.cos(b)

        rotation_matrix_on_Y_axis = np.array([[a,b,c],[d,e,f],[g,h,i]])

        # perform rotation 
        self.actual_position = np.dot(rotation_matrix_on_Y_axis , self.actual_position)

        return self.actual_position

    def rotate_Z_axis(self, radians):
        """ rotate the Y axis with a rotation matrix multiplication 

            |cos(c)     -sin(c)   0|   | x |
            |sin(c)      cos(c)   0| * | y |
            |  0          0       1|   | z | 
        
        """ 

        # rotation matrix creation 
        a,b,c = np.cos(radians), -np.sin(radians), 0
        d,e,f = np.sin(radians),  np.cos(radians), 0
        g,h,i = 0, 0, 1

        rotation_matrix_on_Z_axis = np.array([[a,b,c],[d,e,f],[g,h,i]])


        # perform rotation 
        self.actual_position = np.dot(rotation_matrix_on_Z_axis , self.actual_position)

        return self.actual_position


    def traslate(self, x = 0, y = 0, z = 0):
        """ traslate on X,Y,Z axis of value x,y,z """
        self.actual_position = self.actual_position + np.array([[x],[y],[z]])

    def rototraslate_on_all_axis(self, xradians, yradians, zradians, txradians, tyradians, tzradians):
        """ rototraslate with one method call on all axis. 

            x/y/zradians  fix of how much the rotation need to be applicated
            x/y/ztradians fix of how much the translation need to be applicated
            
        """

        self.rotate_X_axis(xradians)
        self.rotate_Y_axis(yradians)
        self.rotate_Z_axis(zradians)
        self.traslate(txradians, tyradians, tzradians)

        return self.actual_position


def testunit():
    
    rt = geometric_transformation(0,1,0)

    print rt.rotate_X_axis(np.pi/2)
    print rt.rotate_X_axis(-np.pi/2)

    print rt.rotate_Y_axis(np.pi/2)
    print rt.rotate_Y_axis(-np.pi/2)

    print rt.rotate_Z_axis(np.pi/2)
    print rt.rotate_Z_axis(-np.pi/2)


if __name__ == "__main__":
    testunit()

