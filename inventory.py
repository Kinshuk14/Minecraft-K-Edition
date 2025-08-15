from ursina import *

class Inventory(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(0.5, 0.8),
            position=(0, 0),
            texture='white_cube',
            texture_scale=(5, 8),
            color=color.dark_gray
        )

        self.items = []
        for i in range(5):
            for j in range(8):
                item = Button(
                    parent=self,
                    model='quad',
                    scale=(0.18, 0.11),
                    position=(-0.4 + i * 0.2, 0.4 - j * 0.12),
                    color=color.light_gray
                )
                self.items.append(item)