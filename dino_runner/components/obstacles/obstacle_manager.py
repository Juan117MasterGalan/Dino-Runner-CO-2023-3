from dino_runner.components.obstacles.cactus import CactusSmall, CactusLarge
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.heart import Heart
from dino_runner.utils.constants import GAME_SPEED
class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.game_speed = GAME_SPEED

    def update (self, game_speed, player):
        if len(self.obstacles) == 0:
           self.obstacles.append(CactusSmall())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)

        if len(self.obstacles) == 0:
           self.obstacles.append(CactusLarge())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)
            
        if len(self.obstacles) == 0:
           self.obstacles.append(Bird())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)

        if len(self.obstacles) == 0:
           self.obstacles.append(Heart())
        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                self.obstacles.remove(obstacle)
            obstacle.update(game_speed, player)

        
    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)