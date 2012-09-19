
class rototraslator:

    actual_position = ( -1, -1, -1 ) 

    def __init__(self, x, y, z):
        """ set initial position of the object """
        self.actual_position = (x, y, z) 

    def rotate(self, a, ea, b, eb, c, ec):
        """ rotate the object in every axes 

        rotate on axes X of a degree plus an error 'ea'       
        rotate on axes Y of b degree plus an error 'eb'       
        rotate on axes Z of c degree plus an error 'ec' """

    def traslate(self, a, ea, b, eb, c, ec):
        """ traslate the object for every axes """

        

def testunit():
    
    rt = rototraslator(10, 20, 30)
    rt.actual_position



__init__ = testunit()
