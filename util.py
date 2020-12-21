import pygame
import imgs_config
import general_config

pygame.font.init()


def draw_window(win, birds, pipes, base, score, gen, pipe_ind):
    win.blit(imgs_config.BG_IMG, (0, 0))
    for pipe in pipes:
        pipe.draw(win)

    text = pygame.font.SysFont(general_config.FONT_FAMILY, general_config.FONT_SIZE).render(
        f"Score: {score}", 1, (255, 255, 255))
    win.blit(text, (general_config.WIN_WIDTH - 10 - text.get_width(), 10))

    text = pygame.font.SysFont(general_config.FONT_FAMILY, general_config.FONT_SIZE).render(
        f"Gen: {gen}", 1, (255, 255, 255))
    win.blit(text, (10, 10))
    text = pygame.font.SysFont(general_config.FONT_FAMILY, general_config.FONT_SIZE).render(
        f'Alive: {len(birds)}', 1, (255, 255, 255))
    win.blit(text, (10, 50))
    base.draw(win)
    for bird in birds:
        try:
            pygame.draw.line(win, (255, 0, 0), (bird.x+bird.img.get_width()/2, bird.y + bird.img.get_height(
            )/2), (pipes[pipe_ind].x + pipes[pipe_ind].PIPE_TOP.get_width()/2, pipes[pipe_ind].height), 5)
            pygame.draw.line(win, (255, 0, 0), (bird.x+bird.img.get_width()/2, bird.y + bird.img.get_height(
            )/2), (pipes[pipe_ind].x + pipes[pipe_ind].PIPE_BOTTOM.get_width()/2, pipes[pipe_ind].bottom), 5)
        except:
            pass
        bird.draw(win)
    pygame.display.update()
