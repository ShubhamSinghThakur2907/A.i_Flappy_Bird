from class_flappy_bird import *


def main():
    bird = Bird(230, 350)
    base = Base(730)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True 
    while run:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        # bird.move()
        for pipe in pipes:
            pipe.move()
        base.move()
        draw_window(win, bird, pipes, base)

    pygame.quit()
    quit()

main()