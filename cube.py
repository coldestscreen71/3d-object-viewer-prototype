from triangle import Triangle
from transform import Transform
from vec import Vec3

class Mesh:
    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces

    def triangles(self):
        tris = []

        for a, b, c in self.faces:
            tris.append(
                Triangle(
                    self.vertices[a],
                    self.vertices[b],
                    self.vertices[c]
                )
            )

        return tris

class Box(Mesh):
    def __init__(self, width, height, depth):

        w = width / 2
        h = height / 2
        d = depth / 2

        vertices = [
            Vec3(-w,-h,-d),
            Vec3( w,-h,-d),
            Vec3( w, h,-d),
            Vec3(-w, h,-d),

            Vec3(-w,-h, d),
            Vec3( w,-h, d),
            Vec3( w, h, d),
            Vec3(-w, h, d),
        ]

        faces = [

    # Z faces
    (0,1,2), (0,2,3),
    (4,6,5), (4,7,6),

    # X faces
    (0,4,7), (0,7,3),
    (1,6,5), (1,2,6),

    # Y faces
    (3,2,6), (3,6,7),
    (0,5,1), (0,4,5),
    ]

        super().__init__(vertices, faces)

class Object3D:
    def __init__(self, mesh, transform):
        self.mesh = mesh
        self.transform = transform

if __name__ == "__main__":
    pass
