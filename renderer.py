import pygame
from triangle import project
from vec import Vec3
from model import world_transform
from camera import camera_transform

def render(camera, scene, screen, WIDTH, HEIGHT, PROJECTION_SCALE):
    draw_list = []
    for model in scene.models:
        for obj in model.objects:
            wt = world_transform(model, obj)
            ct = camera_transform(camera, wt)
            for tri in obj.mesh.triangles():
                final_tri = ct.apply_triangle(tri)
                ab = final_tri.p2 - final_tri.p1
                ac = final_tri.p3 - final_tri.p1
                normal = ab.cross(ac)
                center = Vec3(
                  (final_tri.p1.x + final_tri.p2.x + final_tri.p3.x) / 3,
                  (final_tri.p1.y + final_tri.p2.y + final_tri.p3.y) / 3,
                  (final_tri.p1.z + final_tri.p2.z + final_tri.p3.z) / 3
                  )
                
                dot = -(
                  normal.x * center.x +
                  normal.y * center.y +
                  normal.z * center.z
                  )
                if dot >= 0:
                    continue
              
                screen_tri = [
                    project(final_tri.p1),
                    project(final_tri.p2),
                    project(final_tri.p3),
                ]
              
                if None in screen_tri:
                    continue
                
                depth = (
                    final_tri.p1.z +
                    final_tri.p2.z +
                    final_tri.p3.z
                ) / 3
                
                points = []
                
                for x, y in screen_tri:

                    points.append(
                    (
                        x * PROJECTION_SCALE + WIDTH // 2,
                        -y * PROJECTION_SCALE + HEIGHT // 2
                    )
                )
                
                draw_list.append(
                    (depth, points)
                )

    draw_list.sort(
        key=lambda item: item[0],
        reverse=True
    )
    for depth, points in draw_list:
        pygame.draw.polygon(
            screen,
            (255, 255, 255),
            points,
            0
        )
        pygame.draw.polygon(
            screen,
            (0,0,0),
            points,
            1
        )