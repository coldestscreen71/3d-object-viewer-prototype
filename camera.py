import math
from transform import Transform

class Camera:
    def __init__(self):
        self.transform = Transform(0,0,0)

    def move(self, x=0, y=0, z=0):
        self.transform.x += x
        self.transform.y += y
        self.transform.z += z
    def rotate(self, rx=0, ry=0, rz=0):

        self.transform.rx += rx
        self.transform.ry += ry
        self.transform.rz += rz

def camera_transform(camera, wt):

    x = wt.x - camera.transform.x
    y = wt.y - camera.transform.y
    z = wt.z - camera.transform.z

    rad = math.radians(-camera.transform.rx)
    y, z = (
        y * math.cos(rad) - z * math.sin(rad),
        y * math.sin(rad) + z * math.cos(rad)
    )

    rad = math.radians(-camera.transform.ry)
    x, z = (
        x * math.cos(rad) + z * math.sin(rad),
        -x * math.sin(rad) + z * math.cos(rad)
    )

    rad = math.radians(-camera.transform.rz)
    x, y = (
        x * math.cos(rad) - y * math.sin(rad),
        x * math.sin(rad) + y * math.cos(rad)
    )

    t = Transform(x, y, z)

    t.rx = wt.rx - camera.transform.rx
    t.ry = wt.ry - camera.transform.ry
    t.rz = wt.rz - camera.transform.rz

    return t