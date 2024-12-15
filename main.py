import pygame.midi
from src.user_interface import MusicAppUI  # Importa a classe da interface
import tkinter as tk

# Inicializa o pygame para MIDI
pygame.midi.init()

# Criação da janela principal do Tkinter
root = tk.Tk()
app = MusicAppUI(root)  # Cria a instância da interface gráfica

# Inicia a interface gráfica
root.mainloop()

# Finaliza o pygame quando a interface for fechada
pygame.midi.quit()
