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

    def generate_music(self, text):
        for char in text:
            action = self.mapper.map_character(char)
            action.execute(self)

    def play_note(self, pitch):
        note = Note(pitch, 0.5, self.volume, self.octave)
        note.play(self.midi_out)

    def adjust_volume(self, value):
        self.volume = min(self.volume * 2, 127) if value == ' ' else 64

    def switch_instrument(self, midi_code):
        self.current_instrument = Instrument("Custom", midi_code)
        self.current_instrument.switch_to(self.midi_out)

    def change_octave(self, increase=True):
        self.octave = min(self.octave + 1, 8) if increase else max(self.octave - 1, 0)

    def pause(self):
        pygame.time.delay(500)
