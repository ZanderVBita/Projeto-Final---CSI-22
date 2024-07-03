import pygame
from utils import blit_text_center

class Menu:
    def __init__(self, win, font):
        self.win = win
        self.font = font

    def display_message(self, message):
        self.win.fill((0, 0, 0))  
        blit_text_center(self.win, self.font, message)
        pygame.display.update()

    def wait_for_keypress(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def show_pause_menu(self):
        self.display_message("Paused. Press C to continue or Q to quit.")
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        waiting = False  # Continue the game
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        exit()
