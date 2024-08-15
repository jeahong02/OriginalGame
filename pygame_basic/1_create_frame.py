import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640 
pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("처음 만드는 게임")

# 이벤트 루프
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
pygame.quit()