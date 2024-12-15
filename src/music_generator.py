# Classe principal de funcionamento do Music Generator
# Possui os atributos como volume, oitava e instrumentos atuais, 
# além dos métodos necessários para alterá-los

import pygame.midi
from src.character_mapper import CharacterMapper
from src.instrument import Instrument
from src.note import Note

class MusicGenerator:
    def __init__(self):
        self.volume = 25
        self.octave = 4
        self.current_instrument = Instrument("Piano", 0)
        self.mapper = CharacterMapper()
        self.midi_out = pygame.midi.Output(0)
        self.current_instrument.switch_to(self.midi_out)

    def generate_music(self, text):
        for char in text:
            action, value = self.mapper.map_character(char)
            match action:
                case 'note':
                    self.play_note(value)
                case 'volume':
                    self.adjust_volume()
                case 'instrument':
                    self.switch_instrument(value)
                case 'octave':
                    if(value == 'up'):
                        self.add_octave()
                    else:
                        self.dec_octave()
                case 'pause':
                    self.pause()

    def play_note(self, pitch_base):
        # Calcula o valor final do pitch somando a base com a oitava
        note = Note(pitch_base, 0.5, self.volume, self.octave)
        note.play(self.midi_out)

    def adjust_volume(self):
        # Dobra o volume até o máximo de 127, ou redefine para 64
        self.volume = min(self.volume * 2, 127) if self.volume < 127 else 25

    def switch_instrument(self, midi_code):
        self.current_instrument = Instrument("Custom", midi_code)
        self.current_instrument.switch_to(self.midi_out)

    def add_octave(self):
        # Sobe uma oitava dentro dos limites do MIDI
        self.octave = min(self.octave + 1, 8)
        print(self.octave)

    def dec_octave(self):
        # Desce uma oitava dentro dos limites do MIDI
        self.octave = max(self.octave - 1, 0)
        print(self.octave)

    def pause(self):
        # Pausa entre ações
        pygame.time.delay(500)

