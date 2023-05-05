import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH

class Bird(Obstacle):
    BIRD_HEIGHTS = [260, 220, 150]
    Y_POS_BIRD =  BIRD_HEIGHTS[random.randint(0, 2)]
    
    def __init__(self):
        self.image = BIRD[0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.y = self.Y_POS_BIRD
        self.bird_rect.x = SCREEN_WIDTH
        super().__init__(self.image)
        self.steps_index = 0
        

    def update(self, game_speed, player):
        self.rect.x -= game_speed
        super().update(game_speed, player)
               

    def draw(self, screen):
        if self.steps_index >= 10:
            self.steps_index = 0
        screen.blit(BIRD[self.steps_index // 5], (self.rect.x, self.rect.y))
        self.steps_index += 1
