# CRIAR A UI

from .music_generator import MusicGenerator

class UserInterface:
    def __init__(self):
        self.generator = MusicGenerator()

    def display(self):
        print("Digite o texto para gerar a música:")
        input_text = input("> ")
        self.generator.generate_music(input_text)
        print("Música gerada com sucesso!")
