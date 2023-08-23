import pygame, sys
from game import Game
from colors import Color


def main():
    pygame.init()
    font = pygame.font.Font(None, 40)
    score = font.render("Score", True, Color.white)
    dark_blue = Color.dark_blue
    next_surface = font.render("Next", True, Color.white)
    game_over_surface = font.render("GAME OVER", True, Color.white)


    score_rect = pygame.Rect(320, 55, 170, 60)
    next_rect = pygame.Rect(320, 215, 170, 180)


    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption("Python Tetris")
    clock = pygame.time.Clock()
    game = Game()
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 500)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if game.game_over == True:
                    game.game_over = False
                    game.reset()
                if event.key == pygame.K_LEFT and game.game_over == False:
                    game.move_left()
                elif event.key == pygame.K_RIGHT and game.game_over == False:
                    game.move_right()
                elif event.key == pygame.K_DOWN and game.game_over == False:
                    game.move_down()
                    game.update_score(0, 5)
                elif event.key == pygame.K_UP and game.game_over == False:
                    game.rotate()
            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()

        score_surface = font.render(str(game.score), True, Color.white)   
        screen.fill(dark_blue)
        screen.blit(score, (365, 20, 50, 50))
        screen.blit(next_surface, (375, 180, 50, 50))
        if game.game_over:
            screen.blit(game_over_surface, (320, 450, 50, 50))
        pygame.draw.rect(screen, Color.light_blue, score_rect, 0, 10)
        pygame.draw.rect(screen, Color.light_blue, next_rect, 0, 10)
        screen.blit(score_surface, score_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
        game.draw(screen)

        pygame.display.update()
        clock.tick(60)
main()