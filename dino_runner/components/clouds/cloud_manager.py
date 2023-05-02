from dino_runner.components.clouds.cloud import Cloud

class CloudManager:
    def __init__(self):
        self.clouds = []

    def update (self, game_speed,):
        if len(self.clouds) == 0:
           self.clouds.append(Cloud())
        for elment in self.clouds:
            if elment.rect.x < -elment.rect.width:
                self.clouds.remove(elment)
            elment.update(game_speed)

    def draw (self, screen):
        for element in self.clouds:
            element.draw(screen)