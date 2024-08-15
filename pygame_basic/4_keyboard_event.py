import pygame

pygame.init()

# 화면 크기 설정
screen_width = 1920
screen_height = 1080
pygame.display.set_mode((screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("처음 만드는 게임")

# 배경 이미지 불러오기 
background = pygame.image.load("C:/Users/rlapa/OneDrive/바탕 화면/OriginalGame/pygame_basic/background.jpg")

# 메인 캐릭터 스프라이트 불러오기
character = pygame.image.load("C:/Users/rlapa/OneDrive/바탕 화면/OriginalGame/pygame_basic/티모.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

# 이벤트 루프
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                to_x -= 5 
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
                
            elif event.key == pygame.K_DOWN:
                to_y += 5
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update()

pygame.quit()