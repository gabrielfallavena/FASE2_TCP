# Classe principal de funcionamento do Music Generator
# Possui os atributos como volume, oitava e instrumentos atuais, 
# além dos métodos necessários para alterá-los

import pygame.midi
from .character_mapper import CharacterMapper
from .instrument import Instrument
from .note import Note

class MusicGenerator:
    def __init__(self):
        self.volume = 64
        self.octave = 4
        self.current_instrument = Instrument("Piano", 0)
        self.mapper = CharacterMapper()
        self.midi_out = pygame.midi.Output(0)

    # Executa a ação correspondente a cada caractere do texto de entrada
    def generate_music(self, input_text):
        for char in input_text:
            action = self.mapper.map_character(char)
            action.execute(self)

    # Toca nota nas devidas condições de momento
    def play_note(self, pitch):
        note = Note(pitch, 0.5, self.volume, self.octave) # (nota, duração, volume, oitava)
        note.play(self.midi_out)

    # Dobra o volume em caso de caractere espaço
    def adjust_volume(self, value): 
        self.volume = min(self.volume * 2, 127) if value == ' ' else 64 

    # Troca instrumento de acordo com o midi_code passado
    def switch_instrument(self, midi_code):
        self.current_instrument = Instrument("Custom", midi_code)
        self.current_instrument.switch_to(self.midi_out)

    # Aumenta ou diminui a oitava
    def change_octave(self, increase=True):
        self.octave = min(self.octave + 1, 8) if increase else max(self.octave - 1, 0)

    def pause(self):
        pygame.time.delay(500)
