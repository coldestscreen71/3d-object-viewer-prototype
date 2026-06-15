3D Object Viewer Prototype

A simple software-rendered 3D object viewer written in Python and Pygame.

This project was created to learn the fundamentals of 3D graphics programming, including transforms, cameras, projection, mesh rendering, and visibility algorithms.

Features

- OBJ file loading
- Camera movement
- Camera rotation
- Triangle-based rendering
- Painter's Algorithm
- Back-face culling
- Model / Scene architecture
- Software rendering using Pygame

Rendering Pipeline

Vec3
↓
Triangle
↓
Mesh
↓
Object3D
↓
Model
↓
Scene
↓
World Transform
↓
Camera Transform
↓
Back-face Culling
↓
Projection
↓
Painter's Algorithm
↓
Screen

Controls

Use the on-screen buttons to:

- Move the camera along X, Y and Z axes
- Rotate the camera around X, Y and Z axes

Usage

Run the viewer and provide an OBJ file:

python main.py model.obj

Example:

python main.py table.obj

Project Structure

main.py            - Application entry point
renderer.py        - Rendering pipeline
camera.py          - Camera system
scene.py           - Scene container
model.py           - Model container
transform.py       - Position and rotation data
cube.py            - Mesh and Object3D classes
triangle.py        - Triangle utilities and projection
vec.py             - 3D vector math
obj_loader.py      - OBJ file loader

Current Limitations

- Software renderer only
- Painter's Algorithm can fail on complex geometry
- No clipping
- No Z-buffer
- No textures
- No lighting

Purpose

The goal of this project was not to create a complete game engine, but to understand how a basic 3D rendering pipeline works from scratch.

Concepts explored include:

- 3D vectors
- Meshes
- Hierarchical transforms
- Camera systems
- Perspective projection
- Face normals
- Back-face culling
- Visibility sorting

Future Plans

A future version may be rebuilt using OpenGL or another graphics API to allow:

- Hardware acceleration
- Z-buffer rendering
- Lighting and shading
- Textures
- More advanced rendering techniques

Author

Rimon