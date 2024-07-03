import pygame
from GameInfo import GameInfo
from PlayerCar import PlayerCar
from ComputerCar import ComputerCar
from utils import *
from Menu import Menu

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer_music.load('Mac DeMarco - Chamber Of Reflection (8-Bit).mp3')
    pygame.mixer.music.play(-1)
    collision_sound = pygame.mixer.Sound("evil-laugh-89423.mp3") 
    run_game(collision_sound)

def run_game(collision_sound):
    run = True
    clock = pygame.time.Clock()
    images = load_images()
    player_car = PlayerCar(2, 4)
    computer_car = ComputerCar(0.8, 4, PATH)
    game_info = GameInfo()
    menu = Menu(WIN, MAIN_FONT)

    
    menu.display_message("Press any key to start the game!")
    menu.wait_for_keypress()
    game_info.start_level()

    while run:
        clock.tick(FPS)
        handle_events(game_info, menu)
        update_game_state(player_car, computer_car, game_info, collision_sound)
        draw(WIN, images, player_car, computer_car, game_info)

        if game_info.game_finished():
            handle_game_finished(game_info, player_car, computer_car, menu)

    pygame.quit()

def load_images():
    return [
        (GRASS, (0, 0)),
        (TRACK, (0, 0)),
        (FINISH, FINISH_POSITION),
        (TRACK_BORDER, (0, 0))
    ]

def handle_events(game_info, menu):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu.show_pause_menu()

def update_game_state(player_car, computer_car, game_info, collision_sound):
    move_player(player_car)
    computer_car.move()
    handle_collision(player_car, computer_car, game_info, collision_sound)

def handle_game_finished(game_info, player_car, computer_car, menu):
    menu.display_message("You won the game!")
    pygame.time.wait(5000)
    game_info.reset()
    player_car.reset()
    computer_car.reset()

if __name__ == "__main__":
    main()
