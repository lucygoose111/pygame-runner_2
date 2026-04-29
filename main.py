import pygame
from random import randint, choice

pygame.init()
screen = pygame.display.set_mode((800, 400))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.wav')
        self.jump_sound.set_volume(0.3)
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def animate_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animate_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_move_1 = pygame.image.load('graphics/fly1.png').convert_alpha()
            fly_move_2 = pygame.image.load('graphics/fly2.png').convert_alpha()
            self.frames = [fly_move_1, fly_move_2]
            y_pos = 210

        if type == 'snail':
            snail_move_1 = pygame.image.load('graphics/snail1.png').convert_alpha()
            snail_move_2 = pygame.image.load('graphics/snail2.png').convert_alpha()            
            self.frames = [snail_move_1, snail_move_2]
            y_pos = 300
        
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1080), y_pos))
    
    def animation_state(self):
        self.index += 0.1
        if self.index >= len(self.frames):
            self.index = 0
        self.image = self.frames[int(self.index)]
    
    def destroy(self):
        global score
        if self.rect.x <= -100:
            self.kill()
            score += 1
    
    def update(self):
        self.animation_state()
        self.destroy()
        self.rect.x -= 6

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle, False):
        obstacle.empty()
        bg_music.fadeout(1000)
        game_active = False
        return False
    else:
        return True

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = font_pixeltype.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())

# Obstacle
obstacle = pygame.sprite.Group()
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# Load images
sky_surf = pygame.image.load('graphics/sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()
font_pixeltype = pygame.font.Font('font/pixeltype.ttf', 50)

game_active = False
start_time = 0
score = 0
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = font_pixeltype.render('Pixel Runner', True, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_ins = font_pixeltype.render('Press enter to start.', False, (111, 196, 169))
game_ins_rect = game_ins.get_rect(center=(400, 320))

bg_music = pygame.mixer.Sound('audio/music.wav')

while True:
    for event in pygame.event.get():
        if event.type == obstacle_timer:
            obstacle.add(Obstacle(choice(['fly', 'snail', 'snail'])))
        
        if not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
                bg_music.play(loops=-1)


        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Draw the background
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))

    if game_active:
                
        # Draw text
        score_surf = font_pixeltype.render(f'Score: {score}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center=(400, 50))
        screen.blit(score_surf, score_rect)

        # Draw player
        player.draw(screen)
        player.update()

        # Draw obstacles
        obstacle.draw(screen)
        obstacle.update()

        game_active = collision_sprite()
    
    else:
        # Draw start/game over screen
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        screen.blit(game_ins, game_ins_rect)

        score_message = font_pixeltype.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 350))

        score = 0

        if score > 0:
            screen.blit(score_message, score_message_rect)
        

    pygame.display.update()
    clock.tick(60)
