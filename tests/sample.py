import pygame
import sys

# 초기 설정
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dynamic Map Loading Game")

# 색상 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 캐릭터 속성
character_size = 40
character_x, character_y = screen_width // 2, screen_height // 2
character_speed = 5

# 맵 설정
tile_size = 100  # 각 타일 크기
map_width, map_height = 2000, 2000  # 전체 맵 크기
visible_tiles = screen_width // tile_size, screen_height // tile_size

def draw_map(offset_x, offset_y):
    """캐릭터 위치에 따라 맵의 일부만 표시"""
    for x in range(0, map_width, tile_size):
        for y in range(0, map_height, tile_size):
            if (x - offset_x < screen_width and y - offset_y < screen_height):
                rect = pygame.Rect(x - offset_x, y - offset_y, tile_size, tile_size)
                pygame.draw.rect(screen, BLUE if (x//tile_size + y//tile_size) % 2 == 0 else WHITE, rect)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키 입력 받아서 캐릭터 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed
    if keys[pygame.K_UP]:
        character_y -= character_speed
    if keys[pygame.K_DOWN]:
        character_y += character_speed

    # 화면 초기화
    screen.fill(WHITE)

    # 맵 그리기 (화면의 중앙에 캐릭터 위치 맞추기)
    draw_map(character_x - screen_width // 2, character_y - screen_height // 2)

    # 캐릭터 그리기
    pygame.draw.rect(screen, (255, 0, 0), (screen_width // 2, screen_height // 2, character_size, character_size))

    # 화면 업데이트
    pygame.display.flip()
    pygame.time.Clock().tick(30)
설명
draw_map 함수: offset_x와 offset_y를 사용하여 캐릭터 위치에 따라 맵의 일부만 화면에 그립니다. 캐릭터가 움직이면 화면도 같이 이동하는 것처럼 보입니다.
캐릭터 이동: 키 입력을 통해 캐릭터의 x, y 좌표를 변경하여 캐릭터가 움직이도록 합니다. 캐릭터는 항상 화면 중앙에 표시되고, 그 주변의 맵만 새로 로딩되며 스크롤됩니다.
