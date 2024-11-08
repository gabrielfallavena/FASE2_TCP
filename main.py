import pygame
import pygame.midi
from music_generator.user_interface import UserInterface

def main():
    # Inicializa pygame e pygame.midi
    pygame.init()
    pygame.midi.init()
    
    ui = UserInterface()
    ui.display()

    # Finaliza pygame e pygame.midi
    pygame.midi.quit()
    pygame.quit()

if __name__ == "__main__":
    main()
