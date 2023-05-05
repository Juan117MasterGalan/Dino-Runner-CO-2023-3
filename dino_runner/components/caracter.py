from dino_runner.utils.constants import BIRD_CARACTER
import pygame

class Bird_caracter:
    X_POS_BIRD = 80
    Y_POS_BIRD = 295
    FLY_UP_VEL = 8.5


    def __init__(self):
        self.image = BIRD_CARACTER[0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.y = self.Y_POS_BIRD
        self.bird_rect.x = self.X_POS_BIRD
        self.bird_steps_index = 0
        self.bird_fly = True
        self.bird_fly_up = False
        self.fly_up_vel = self.FLY_UP_VEL
        
    def update(self, user_input):
        if self.bird_fly:
            self.fly()
        if self.bird_fly_up:
            self.fly_up()

        if user_input[pygame.K_UP] and not self.bird_fly_up:
            self.bird_fly = False
            self.bird_fly_up = True
        
        if self.steps_index >= 10:
            self.steps_index = 0
    
    def draw(self, screen):
        screen.blit(self.image, self.bird_rect)

    def fly(self):
        self.image = self.image[0] if self.bird_steps_index < 5 else self.image[1]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = self.X_POS_BIRD
        self.bird_rect.y = self.Y_POS_BIRD
        self.bird_steps_index +=1

    def fly_up(self):
        self.image = self.image[0]
        if self.bird_fly_up:
            self.bird_rect.y -= self.fly_up_vel * 4
            self.fly_up_vel -= 0.8



