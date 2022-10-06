class Vector3D(object):
    x = 0
    y = 0
    z = 0
    modulus = 0
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.modulus = (x**2+y**2+z**2)**0.5 # Gets the square root of the sum of the squares of the coords.
    def get_x(self):
        return self.x
    def __add__(self, other):
        assert type(other) == Vector3D, 'Cannot calculate the distance between '+str(type(self))+' and '+str(type(other))
        return Vector3D(self.x+other.x, self.y+other.y,self.z+other.z)
    def __sub__(self, other):
        assert type(other) == Vector3D, 'Cannot calculate the distance between '+str(type(self))+' and '+str(type(other))
        return Vector3D(self.x-other.x, self.y-other.y,self.z-other.z)
    def __eq__(self,other):
        assert type(other) == Vector3D, 'Cannot calculate the distance between '+str(type(self))+' and '+str(type(other))
        if ((self.x - other.x == 0) and (self.y - other.y == 0) and (self.z - other.z == 0)): return True
        else: return False
    def distanceTo(self, other) -> float:
        assert type(other) == Vector3D, 'Cannot calculate the distance between '+str(type(self))+' and '+str(type(other))
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self) -> str:
        return '<'+str(self.x)+','+str(self.y)+','+str(self.z)+'>'

V = Vector3D(1,1,1)
W = Vector3D(1,1,1)
