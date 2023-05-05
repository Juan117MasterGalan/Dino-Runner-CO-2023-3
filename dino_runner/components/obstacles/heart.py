from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import HEART

class Heart(Obstacle):
    Y_POS_HEART =  125
    
    def __init__(self):
        self.image = HEART
        super().__init__(self.image)
        self.rect.y = self.Y_POS_HEART