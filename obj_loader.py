from cube import Mesh
from vec import Vec3

def load_obj(path):

    vertices = []
    faces = []

    with open(path, "r") as file:

        for line in file:

            if line.startswith("v "):

                _, x, y, z = line.split()

                vertices.append(
                    Vec3(
                        float(x),
                        float(y),
                        float(z)
                    )
                )

            elif line.startswith("f "):

                parts = line.split()[1:]

                face = []

                for p in parts:

                    index = int(
                        p.split("/")[0]
                    ) - 1

                    face.append(index)

                # Triangles

                if len(face) == 3:

                    faces.append(
                        (face[0], face[1], face[2])
                    )

                # Quads

                elif len(face) == 4:

                    faces.append(
                        (face[0], face[1], face[2])
                    )

                    faces.append(
                        (face[0], face[2], face[3])
                    )

    return Mesh(
        vertices,
        faces
    )