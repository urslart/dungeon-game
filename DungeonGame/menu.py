import pygame, sys
from save_system import load_game

pygame.init()
FONT = pygame.font.SysFont("arial", 40)

def draw_text(text, y, selected=False):
    color = (255, 255, 255)
    if selected:
        color = (255, 215, 0)
    return FONT.render(text, True, color), (400, y)

def main_menu(WIN):
    clock = pygame.time.Clock()
    options = ["Start New Game", "Load Game", "Quit"]
    selected_index = 0

    while True:
        WIN.fill((20, 20, 20))
        title = FONT.render("Dungeon Game", True, (0, 200, 200))
        WIN.blit(title, (250, 100))

        for i, text in enumerate(options):
            txt_surf, pos = draw_text(text, 250 + i * 60, i == selected_index)
            WIN.blit(txt_surf, txt_surf.get_rect(center=pos))

        pygame.display.update()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected_index == 0:
                        return "new"
                    elif selected_index == 1:
                        data = load_game()
                        if data:
                            return "load"
                        else:
                            print("No saved game found.")
                    elif selected_index == 2:
                        pygame.quit()
                        sys.exit()
