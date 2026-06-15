import math
from triangle import Triangle
from vec import Vec3

class Transform:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
        self.rx = 0
        self.ry = 0
        self.rz = 0
    
    def apply(self, point):
        x = point.x
        y = point.y
        z = point.z
        # Rotate X
        rad = math.radians(self.rx)
        y, z = (
            y * math.cos(rad) - z * math.sin(rad),
            y * math.sin(rad) + z * math.cos(rad)
        )
        # Rotate Y
        rad = math.radians(self.ry)
        x, z = (
            x * math.cos(rad) + z * math.sin(rad),
            -x * math.sin(rad) + z * math.cos(rad)
        )
        # Rotate Z
        rad = math.radians(self.rz)
        x, y = (
            x * math.cos(rad) - y * math.sin(rad),
            x * math.sin(rad) + y * math.cos(rad)
        )
        # Translate
        x += self.x
        y += self.y
        z += self.z
        return Vec3(x, y, z)
    
    def apply_triangle(self, triangle):
        return Triangle(
            self.apply(triangle.p1),
            self.apply(triangle.p2),
            self.apply(triangle.p3)
        )