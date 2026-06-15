import math

from cube import Object3D, Box
from transform import Transform
from triangle import project

class Model:
    def __init__(self):
        self.objects = []
        self.transform = Transform(0,0,0)

    def add(self, obj):
        self.objects.append(obj)

    def move(self, x=0, y=0, z=0):
        self.transform.x += x
        self.transform.y += y
        self.transform.z += z

    def rotate(self, rx=0, ry=0, rz=0):
        self.transform.rx += rx
        self.transform.ry += ry
        self.transform.rz += rz

def world_transform(model, obj):

    x = obj.transform.x
    y = obj.transform.y
    z = obj.transform.z

    # ---------- Rotate X ----------

    rad = math.radians(model.transform.rx)

    y, z = (
        y * math.cos(rad) - z * math.sin(rad),
        y * math.sin(rad) + z * math.cos(rad)
    )

    # ---------- Rotate Y ----------

    rad = math.radians(model.transform.ry)

    x, z = (
        x * math.cos(rad) + z * math.sin(rad),
        -x * math.sin(rad) + z * math.cos(rad)
    )

    # ---------- Rotate Z ----------

    rad = math.radians(model.transform.rz)

    x, y = (
        x * math.cos(rad) - y * math.sin(rad),
        x * math.sin(rad) + y * math.cos(rad)
    )

    # ---------- Parent Translation ----------

    x += model.transform.x
    y += model.transform.y
    z += model.transform.z

    # ---------- Build Final Transform ----------

    t = Transform(x, y, z)

    t.rx = model.transform.rx + obj.transform.rx
    t.ry = model.transform.ry + obj.transform.ry
    t.rz = model.transform.rz + obj.transform.rz

    return t