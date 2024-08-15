import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640 
pygame.display.set_mode((screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("처음 만드는 게임")

# 배경 이미지 불러오기 
background = pygame.image.load("C:/Users/rlapa/OneDrive/바탕 화면/OriginalGame/pygame_basic/Background.png")

# 이벤트 루프
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.blit(background, (0, 0))
    
    pygame.display.update()

pygame.quit()