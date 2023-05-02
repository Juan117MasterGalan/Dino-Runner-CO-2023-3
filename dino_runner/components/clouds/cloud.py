import random
from dino_runner.components.clouds.element import Element
from dino_runner.utils.constants import CLOUD

class Cloud(Element):
    Y_POS_CLOUD = random.randiant (10, 300)

    def __init__(self):
        self.image = CLOUD
        super().__init__(self.image)
        self.rect.y = self.Y_POS_CLOUD