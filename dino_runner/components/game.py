import pygame
import random
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, RESET
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.caracter import Bird_caracter
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components import text_utils
from dino_runner.utils.constants import GAME_SPEED

class Game:
    frames_clouds = 0
    clouds = []
    for i in range (6):
        x_pos_cloud = 1000
        y_pos_cloud = random.randint(0, 300)
        speed_cloud = random.randint(1, 8)
        list_clouds = [x_pos_cloud, y_pos_cloud, speed_cloud]
        clouds.append(list_clouds)


    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Bird_caracter()
        self.obstacle_manager = ObstacleManager()    
        self.power_up_manager = PowerUpManager()    
        self.points = 0 
        self.death_count = 0


    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            #pygame.mixer.music.load(TEMAZO) == 0
            #pygame.mixer.music.play(-1)
            self.events()
            self.update()
            self.draw()
        pygame.quit()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset_game()


    def update(self):
        if self.playing:
           self.points +=1
           user_input = pygame.key.get_pressed()
           self.player.update(user_input)
           self.obstacle_manager.update(self.game_speed, self.player)
           self.power_up_manager.update(self.game_speed, self.points, self.player)
           if self.player.dino_dead:
               self.playing = False
               self.death_count +=1


    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_background()
            self.draw_score()
            self.player.draw(self.screen)
            self.obstacle_manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)
        else: 
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()
        

    def draw_background(self):
        for a in self.clouds:
            a[0] -= a[2]
            if a[0] < -200:
                a[0] = 1200
                a[1] = random.randint(0, 360)
                a[2] = random.randint(1, 8)
                
        self.frames_clouds += 1
        if self.frames_clouds >= 71:
            self.frames_clouds = 1
        if self.frames_clouds < 11:
            for a in self.clouds:
                self.screen.blit(CLOUD, (a[0], a[1]))
        if self.frames_clouds < 31:
            for a in self.clouds:
                self.screen.blit(CLOUD, (a[0], a[1]))
        if self.frames_clouds < 51:
            for a in self.clouds:
                self.screen.blit(CLOUD, (a[0], a[1]))
        if self.frames_clouds < 71:
            for a in self.clouds:
                self.screen.blit(CLOUD, (a[0], a[1]))

        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


    def draw_score (self):
        score, score_text = text_utils.get_message("points " + str(self.points), 20, 1000, 40)
        self.screen.blit(score, score_text)


    def draw_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        if self.death_count == 0:
            text, text_rect = text_utils.get_message("Press any key to Start", 30)
            self.screen.blit(text, text_rect)
        else:
            pygame.display.set_icon(RESET)
            text, text_rect = text_utils.get_message("Press any key to Resert", 30)
            score, score_rect = text_utils.get_message("Your score: " + str(self.points), 30, height= SCREEN_HEIGHT//2 + 50)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)


    def reset_game(self):
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
