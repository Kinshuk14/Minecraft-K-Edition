from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

app = Ursina()

# Player settings
jump_height = 4.0 #10
jump_duration = 1.0 #0.90
jump_fall_after = 0.60 #0.36
gravity_scale = 1 #1
mouse_sensitivity = Vec2(40,40)
run_speed = 15.0 #2

window.fps_counter.enabled = False
window.exit_button.visible = False

# Sound
punch = Audio('assets/punch', autoplay=False)

# Block textures
blocks = [
    load_texture('assets/grass.png'),  # 0
    load_texture('assets/grass.png'),  # 1 (default block)
    load_texture('assets/stone.png'),  # 2
    load_texture('assets/gold.png'),   # 3
    load_texture('assets/lava.png'),   # 4
    load_texture('assets/leaves.png'), # 5
    load_texture('assets/wood.png'),   # 6
]

block_id = 1  # default block index

# Input for switching block type
def input(key):
    global block_id, hand
    if key.isdigit():
        block_id = int(key)
        if block_id >= len(blocks):
            block_id = len(blocks) - 1
        hand.texture = blocks[block_id]

# Sky using your custom sky texture
sky = Entity(
    parent=scene,
    model='sphere',
    texture=load_texture('assets/sky.png'),
    scale=1000,
    double_sided=True
)

# Player hand
hand = Entity(
    parent=camera.ui,
    model='assets/block',
    texture=blocks[block_id],
    scale=0.2,
    rotation=Vec3(-10, -10, 10),
    position=Vec2(0.6, -0.6)
)

def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
        punch.play()
        hand.position = Vec2(0.4, -0.5)
    else:
        hand.position = Vec2(0.6, -0.6)

    if player.y < -10:
        player.position = Vec3(10, 5, 10)

# Block class
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='assets/grass.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
            elif key == 'right mouse down':
                destroy(self)

# World Generation
# 25x25 Pre-designed world with 3 layers
WORLD_SIZE = 25

# Create terrain (2 stone layers + 1 grass layer)
for x in range(WORLD_SIZE):
    for z in range(WORLD_SIZE):
        Voxel(position=(x, -3, z), texture=blocks[2])  # Stone base
        Voxel(position=(x, -2, z), texture=blocks[4])  # Stone base
        Voxel(position=(x, -1, z), texture=blocks[2])  # Stone base
        Voxel(position=(x, 0, z), texture=blocks[2])   # Stone middle
        Voxel(position=(x, 1, z), texture=blocks[0])   # Grass
        
def create_tree(position):
    # Trunk
    for i in range(6):
        Voxel(position=position + Vec3(0, i, 0), texture=blocks[6])
    # Leaves
    for x in range(-2, 3):
        for y in range(4, 8):
            for z in range(-2, 3):
                if not (x == 0 and z == 0) or y > 6:
                    if random.randint(0, 1) == 0:
                        Voxel(position=position + Vec3(x, y, z), texture=blocks[5])

create_tree(Vec3(randint(0, 19), 1, randint(0, 19)))
create_tree(Vec3(randint(0, 19), 1, randint(0, 19)))
create_tree(Vec3(randint(0, 19), 1, randint(0, 19)))

# Player controller
player = FirstPersonController()
player.jump_height = jump_height
player.jump_up_duration = jump_duration
player.mouse_sensitivity = mouse_sensitivity
player.speed = run_speed
player.gravity = gravity_scale
player.position = Vec3(0, 0, 0)

app.run()
