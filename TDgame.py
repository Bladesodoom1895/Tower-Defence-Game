import pygame

pygame.font.init()

s_width = 1000
s_height = 800
play_width = 800
play_height = 600

top_left_x = (s_width - play_width) / 2
top_left_y = (s_height - play_height) / 2

rows = 30
columns = 20

def __init__(self, column, row,):
    self.x = column
    self.y = row

def create_grid(locked_positions={}):
    grid = [[(0, 0, 0,) for x in range(30)] for y in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid

def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2),
                 top_left_y + play_height / 2 - label.get_height() / 2))

def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * 20),
                         (sx + play_width, sy + i * 20))
        for j in range(col):
            pygame.draw.line(surface, (128, 128, 128), (sx + j * 20, sy),
                             (sx + j * 20, sy + play_height))
# Controls Grid square size

def draw_window(surface):
    surface.fill((20, 20, 20))

    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tower Defence', 1, (255, 255, 255))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2),
                 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j * 20,
                             top_left_y + i * 20, 220, 220), 0)
# Controls Background color

    draw_grid(surface, 30, 40) # Controls number of sqaures y, x
    pygame.draw.rect(surface, (255, 255, 255), (top_left_x, top_left_y,
                     play_width, play_height), 5)
    pygame.display.update()

def main():
    global grid

    locked_positions = {}
    grid = create_grid(locked_positions)

    run = True

    while run:
        grid = create_grid(locked_positions)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

        draw_window(win)
        pygame.display.update()

def main_menu():
    run = True
    while run:
        win.fill((20, 20, 20))
        draw_text_middle('Press any key to begin.', 60, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN or pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tower Defence')

main_menu()