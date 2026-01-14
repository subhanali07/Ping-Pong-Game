import pygame
import sys

pygame.init()

width, height=800, 500
screen= pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")

white= (255,255,255)
black= (0,0,0)
clock= pygame.time.Clock()
font= pygame.font.SysFont("Arial", 40)

paddle_width, paddle_height= 15, 100
left_paddle= pygame.Rect(30, height//2 - 50, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 45, height//2 - 50, paddle_width, paddle_height)

ball= pygame.Rect(width//2 - 10, height//2 - 10, 20, 20)
ball_x_speed= 2
ball_y_speed= 2
left_score= 0
right_score= 0

game_active= True
def reset_ball():
     global ball_x_speed, ball_y_speed, game_active
     ball.center = (width // 2, height // 2)
     ball_x_speed = 5
     ball_y_speed = 5
     game_active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                  game_active = True

    keys=pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= 7
    if keys[pygame.K_s] and left_paddle.bottom < height:
        left_paddle.y += 7
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= 7
    if keys[pygame.K_DOWN] and right_paddle.bottom < height:
            right_paddle.y += 7

    if game_active:
         ball.x += ball_x_speed
         ball.y += ball_y_speed

    if ball.top <= 0 or ball.bottom >= height:
         ball_y_speed *= -1

    
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
         ball_x_speed *= -1

    if ball.left <= 0:
         right_score += 1
         reset_ball()
    if ball.right >= width:
         left_score += 1
         reset_ball()

    
    screen.fill(black)
    pygame.draw.rect(screen, white, left_paddle)
    pygame.draw.rect(screen, white, right_paddle)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (width//2, 0), (width//2, height))

    left_text= font.render(str(left_score), True, white)
    right_text= font.render(str(right_score), True, white)
    screen.blit(left_text, (width//2 - 60, 20))
    screen.blit(right_text, (width//2 + 30, 20))
    
    if not game_active:
         msg = font.render("Press Space to Play", True, white)
         screen.blit(msg, (width//2 - 200, height//2 - 20))

    pygame.display.flip()
    clock.tick(60)