import pygame
from GameInfo import GameInfo
from PlayerCar import PlayerCar
from ComputerCar import ComputerCar
from utils import *
from Menu import Menu



def main():
    pygame.init()
    pygame.mixer_music.load('Projeto-Final---CSI-22/Mac DeMarco - Chamber Of Reflection (8-Bit).mp3')
    pygame.mixer.music.play(-1)
    run_game()

def run_game():
    run = True
    clock = pygame.time.Clock()
    images = load_images()
    player_car = PlayerCar(4, 4)
    computer_car = ComputerCar(2, 4, PATH)
    game_info = GameInfo()
    menu = Menu(WIN, MAIN_FONT)

    while run:
        clock.tick(FPS)
        handle_events(game_info, menu)
        update_game_state(player_car, computer_car, game_info)
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
            if not game_info.started:
                menu.display_message(f"Press any key to start level {game_info.level}!")
                menu.wait_for_keypress()
                game_info.start_level()

def update_game_state(player_car, computer_car, game_info):
    move_player(player_car)
    computer_car.move()
    handle_collision(player_car, computer_car, game_info)

def handle_game_finished(game_info, player_car, computer_car, menu):
    menu.display_message("You won the game!")
    pygame.time.wait(5000)
    game_info.reset()
    player_car.reset()
    computer_car.reset()

if __name__ == "__main__":
    main()
