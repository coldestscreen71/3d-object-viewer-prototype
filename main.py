import sys
import pygame

from cube import Object3D
from model import Model
from transform import Transform
from scene import Scene
from camera import Camera
from renderer import render
from obj_loader import load_obj

pygame.init()

# ---------------- WINDOW ----------------

WIDTH = 1200
HEIGHT = 800
PROJECTION_SCALE = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Object Viewer")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

# ---------------- LOAD MODEL ----------------

if len(sys.argv) < 2:
    print("Usage:")
    print("python main.py model.obj")
    quit()

obj_path = sys.argv[1]

mesh = load_obj(obj_path)

obj = Object3D(
    mesh,
    Transform(0, 0, 0)
)

model = Model()

model.add(obj)

model.transform.z = 4

# ---------------- SCENE ----------------

scene = Scene()
scene.add_model(model)

camera = Camera()

# ---------------- BUTTONS ----------------

buttons = {

    # Position

    "x+": pygame.Rect(20, 20, 70, 45),
    "x-": pygame.Rect(100, 20, 70, 45),

    "y+": pygame.Rect(20, 80, 70, 45),
    "y-": pygame.Rect(100, 80, 70, 45),

    "z+": pygame.Rect(20, 140, 70, 45),
    "z-": pygame.Rect(100, 140, 70, 45),

    # Rotation

    "rx+": pygame.Rect(250, 20, 70, 45),
    "rx-": pygame.Rect(330, 20, 70, 45),

    "ry+": pygame.Rect(250, 80, 70, 45),
    "ry-": pygame.Rect(330, 80, 70, 45),

    "rz+": pygame.Rect(250, 140, 70, 45),
    "rz-": pygame.Rect(330, 140, 70, 45),
}

# ---------------- DRAW BUTTONS ----------------

def draw_buttons():

    for text, rect in buttons.items():

        pygame.draw.rect(
            screen,
            (70, 70, 70),
            rect
        )

        label = font.render(
            text,
            True,
            (255, 255, 255)
        )

        screen.blit(
            label,
            (
                rect.x + 15,
                rect.y + 10
            )
        )

# ---------------- HANDLE BUTTONS ----------------

def handle_button(name):

    if name == "x+":
        camera.move(1, 0, 0)

    elif name == "x-":
        camera.move(-1, 0, 0)

    elif name == "y+":
        camera.move(0, 1, 0)

    elif name == "y-":
        camera.move(0, -1, 0)

    elif name == "z+":
        camera.move(0, 0, 1)

    elif name == "z-":
        camera.move(0, 0, -1)

    elif name == "rx+":
        camera.rotate(2, 0, 0)

    elif name == "rx-":
        camera.rotate(-2, 0, 0)

    elif name == "ry+":
        camera.rotate(0, 2, 0)

    elif name == "ry-":
        camera.rotate(0, -2, 0)

    elif name == "rz+":
        camera.rotate(0, 0, 2)

    elif name == "rz-":
        camera.rotate(0, 0, -2)

# ---------------- MAIN LOOP ----------------

running = True

while running:

    # ---------- EVENTS ----------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()

            for name, rect in buttons.items():

                if rect.collidepoint(mouse_pos):
                    handle_button(name)

    # ---------- CLEAR ----------

    screen.fill((20, 20, 20))

    # ---------- UI ----------

    draw_buttons()

    # ---------- RENDER ----------

    render(
        camera,
        scene,
        screen,
        WIDTH,
        HEIGHT,
        PROJECTION_SCALE
    )

    # ---------- DEBUG ----------

    pos_text = font.render(
        f"Position: "
        f"({round(camera.transform.x,2)}, "
        f"{round(camera.transform.y,2)}, "
        f"{round(camera.transform.z,2)})",
        True,
        (255, 255, 255)
    )

    screen.blit(pos_text, (20, 250))

    rot_text = font.render(
        f"Rotation: "
        f"({round(camera.transform.rx,2)}, "
        f"{round(camera.transform.ry,2)}, "
        f"{round(camera.transform.rz,2)})",
        True,
        (255, 255, 255)
    )

    screen.blit(rot_text, (20, 290))

    # ---------- UPDATE ----------

    pygame.display.flip()

    clock.tick(60)

pygame.quit()