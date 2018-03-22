import pygame
import random
 
pygame.init()
BALL_IMAGE = pygame.image.load('geschoss.png')

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
PADDLE_X = 30
PADDLE_Y = 120
PADDLE_DISTANCE = 30
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen_size_info = pygame.display.Info()
SCREEN_SIZE = (screen_size_info.current_w, screen_size_info.current_h)
font = pygame.font.SysFont("comicsansms", 40)
clock = pygame.time.Clock()
score_player_1 = 0
score_player_2 = 0
balls = 3
paddle_left_group  = pygame.sprite.Group()
paddle_right_group = pygame.sprite.Group()

def init():
    global score_player_1
    global score_player_2
    global balls
    score_player_1 = 0
    score_player_2 = 0
    balls = 3

run = True
w_down = False
s_down = False
kup_down = False
kdown_down = False
hit1 = False
hit2 = False
class paddle(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([PADDLE_X, PADDLE_Y])
        self.rect = self.image.get_rect()
        self.x_size = PADDLE_X
        self.y_size = PADDLE_Y
        if position == 'left':
            x = PADDLE_DISTANCE
        else:
            x = SCREEN_SIZE[0]-PADDLE_DISTANCE
        self.rect.center = (x,SCREEN_SIZE[1]/2)
        self.move_speed = 15
    def update(self,increment):
        if self.rect.bottom > SCREEN_SIZE[1]:
            self.rect.bottom = SCREEN_SIZE[1]
        if self.rect.y < 0:
            self.rect.y = 0
        self.rect.y += increment 
        
    def draw(self):
        pygame.draw.rect(screen,
                         BLACK,
                         (self.rect.x,self.rect.y,self.x_size,self.y_size))
        
class ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = BALL_IMAGE
        self.x_size = self.image.get_width()
        self.y_size = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_SIZE[0]-self.x_size)/2.
        self.rect.y = (SCREEN_SIZE[1]-self.y_size)/2.
        self.xspeed = 3
        self.yspeed = 2
        
    def move(self):        
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        
    def reset(self):
        self.rect.x = (SCREEN_SIZE[0]-self.x_size)/2.
        self.rect.y = (SCREEN_SIZE[1]-self.y_size)/2.
        self.xspeed = 3
        self.yspeed = 2
        
    def collide_check(self,paddle_left,paddle_right):
        balls = 0
        score_player_1 = 0
        score_player_2 = 0
        if self.rect.right < 0:
            score_player_2 = 1
            balls = -1
            self.reset()
        if self.rect.left > SCREEN_SIZE[0]:
            score_player_1 = 1
            balls = -1
            self.reset()
            
        if self.rect.top < 0:
            self.rect.top = -self.rect.top
            if self.yspeed < 0:
                self.yspeed -= random.randint(0,2)
                self.yspeed *= -1
            else:
                self.yspeed += random.randint(0,2)
                self.yspeed *= -1
            if self.xspeed < 0:
                self.xspeed-=random.randint(0,2)
            else:
                self.xspeed+=random.randint(0,2)
        if self.rect.bottom > SCREEN_SIZE[1]:
            self.rect.bottom = 2*SCREEN_SIZE[1]-self.rect.bottom
            if self.yspeed < 0:
                self.yspeed -= random.randint(0,2)
                self.yspeed *= -1
            else:
                self.yspeed += random.randint(0,2)
                self.yspeed *= -1
            if self.xspeed < 0:
                self.xspeed-=random.randint(0,2)
            else:
                self.xspeed+=random.randint(0,2)
        return score_player_1, score_player_2, balls

ball1 = ball()

pad_left  = paddle('left')
pad_right = paddle('right')

paddle_left_group.add(pad_left)
paddle_right_group.add(pad_right)



#Main loop
while run:      
    down_keys = pygame.key.get_pressed()
    if down_keys[pygame.K_DOWN]:
        pad_right.update(pad_right.move_speed)
    if down_keys[pygame.K_UP]:
        pad_right.update(-pad_right.move_speed)
    if down_keys[pygame.K_w]:
        pad_left.update(-pad_left.move_speed)
    if down_keys[pygame.K_s]:
        pad_left.update(pad_left.move_speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False      
    player1 = font.render('Punkte:' + str(score_player_1), True, BLUE)
    baelle  = font.render('Baelle:' + str(balls),          True, BLUE)
    player2 = font.render('Punkte:' + str(score_player_2), True, BLUE)
    p1,p2,b = ball1.collide_check(pad_left, pad_right)
    balls += b
    if balls == 0:
        balls = 'Over'
        run = False 
    score_player_1 += p1
    score_player_2 += p2
    ball1.move()
    screen.fill(WHITE)
    screen.blit(ball1.image,ball1.rect)
    screen.blit(player1,(300,30))
    screen.blit(player2,(1000,30))
    screen.blit(baelle,(5,30))
    pad_left.draw()
    pad_right.draw()
    if pygame.sprite.spritecollide(ball1, paddle_left_group,False):
        ball1.xspeed =-(ball1.xspeed-1)
    if pygame.sprite.spritecollide(ball1,paddle_right_group,False):
        ball1.xspeed =-(ball1.xspeed+1)
    pygame.display.flip()
    clock.tick(50)
pygame.time.delay(1000)
pygame.quit()