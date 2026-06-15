import math
from vec import Vec3

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.points_list = [p1, p2, p3]
    
    def points(self):
        return [
          self.p1.points(),
          self.p2.points(),
          self.p3.points(),
          ]

def project(point):
    if point.z <= 0.010:
        return None
    return (
        point.x / point.z,
        point.y / point.z
    )

if __name__ == "__main__":
    from transform import Transform
    p1 = Vec3(0, 1, 0)
    p2 = Vec3(-0.866, -0.5, 0)
    p3 = Vec3(0.866, -0.5, 0)
    #let's say for now
    cube_x = 3
    cube_y = 3
    cube_z = 3
    t = Transform(cube_x, cube_y, cube_z)
    tri = Triangle(p1, p2, p3)
    world_tri = t.apply_triangle(tri)
    screen_tri = [
    project(world_tri.p1),
    project(world_tri.p2),
    project(world_tri.p3),
]
    print(screen_tri)