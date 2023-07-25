import pygame

from Button import Button
from SortingList import SortingList


#constants
LIST_SIZE = 250
WIDTH = 1280
HEIGHT = 720
BUTTON_WIDTH = WIDTH * 0.2
BUTTON_HEIGHT = HEIGHT * 0.1
BUTTON_ALIGN_CENTER = WIDTH * 0.5 - BUTTON_WIDTH / 2
BUTTON_ALIGN_HEIGHT = HEIGHT * 0.9 - BUTTON_HEIGHT / 2


#flags
running = True
hovering = False


#setup
algorithm = "quicksort"
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting visualisation")

sorting_list = SortingList(window, LIST_SIZE, [WIDTH * 0.05, HEIGHT * 0.1, WIDTH * 0.90, HEIGHT * 0.6])
button_list = []

shuffle_button = Button(window, (220, 0, 0), [BUTTON_ALIGN_CENTER - BUTTON_WIDTH * 0.6,
                                   BUTTON_ALIGN_HEIGHT,
                                   BUTTON_WIDTH, BUTTON_HEIGHT], sorting_list.shuffle, (255, 0, 0))

sort_button = Button(window, (0, 220, 0), [BUTTON_ALIGN_CENTER + BUTTON_WIDTH * 0.6,
                                   BUTTON_ALIGN_HEIGHT,
                                   BUTTON_WIDTH, BUTTON_HEIGHT], lambda: sorting_list.sort(algorithm), (0, 255, 0))

button_list.append(shuffle_button)
button_list.append(sort_button)


#app
while running:
    window.fill("black")
    mouse_position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for button in button_list:
                    if button.hover(mouse_position):
                        button.callback()

    sorting_list.draw()

    for button in button_list:
        button.draw()
        if button.hover(mouse_position):
            hovering = True

    if hovering:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        hovering = False
    else: pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    pygame.display.update()

pygame.quit()