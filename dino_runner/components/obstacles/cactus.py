import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class CactusSmall(Obstacle):
    Y_POS_CACTUSSMALL =  325
    
    def __init__(self):
        self.image = random.choice(SMALL_CACTUS)
        super().__init__(self.image)
        self.rect.y = self.Y_POS_CACTUSSMALL

class CactusLarge(Obstacle):
    Y_POS_CACTUSLARGE = 300

    def __init__(self):
        self.image = random.choice(LARGE_CACTUS)
        super().__init__(self.image)
        self.rect.y = self.Y_POS_CACTUSLARGE
