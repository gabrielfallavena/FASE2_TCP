import customtkinter as ctk
from src.user_interface import MusicAppUI
import pygame.midi 

ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("blue") 

def main():
    # Inicializa o sistema MIDI
    pygame.midi.init()
    try:
        # Cria a instância da interface gráfica
        app = MusicAppUI()
        app.mainloop()  # Inicia o loop principal do Tkinter
    finally:
        # Finaliza o sistema MIDI ao sair do programa
        pygame.midi.quit()

if __name__ == "__main__":
    main()
