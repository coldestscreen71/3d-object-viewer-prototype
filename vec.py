class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def points(self):
        return [self.x, self.y, self.z]
    
    def __sub__(self, other):
        return Vec3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )
    
    def cross(self, other):
          return Vec3(
              self.y * other.z - self.z * other.y,
              self.z * other.x - self.x * other.z,
              self.x * other.y - self.y * other.x
          )