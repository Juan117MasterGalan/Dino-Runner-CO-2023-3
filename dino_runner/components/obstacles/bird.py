import random, pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH, DINODEAD
from dino_runner.components.dinosaur import Dinosaur

class Bird(Obstacle):
    BIRD_HEIGHTS = [260, 220, 170]
    Y_POS_BIRD =  random.choice(BIRD_HEIGHTS)
    
    def __init__(self):
        self.image = BIRD[0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.y = self.Y_POS_BIRD
        self.bird_rect.x = SCREEN_WIDTH
        super().__init__(self.image)
        self.steps_index = 0
        

    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if self.image == BIRD[0] or self.image == BIRD[1]:
            self.image == BIRD[0] if self.steps_index < 5 else BIRD[1]
            self.steps_index +=1
            if self.steps_index >= 10:
                self.steps_index = 0
        super().update(game_speed, player)
               

    def draw(self, screen):
        screen.blit(self.image, self.bird_rect)
