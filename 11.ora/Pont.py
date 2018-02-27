from math import sqrt, pow

class Pont2D:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pont3D(Pont2D):
    def __init__(self, x, y, z):
        self.z = z
        super().__init__(x, y)
    
    def __str__(self):
        return "X: {}, Y: {}, Z: {}".format(self.x, self.y, self.z)

a = Pont2D(2,3)
b = Pont3D(2,3,4)

print(a)
print(b)