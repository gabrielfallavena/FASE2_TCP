# Contém os atributos de uma nota e seu método de play

import pygame

class Note:
    def __init__(self, pitch, duration, volume, octave):
        self.pitch = pitch
        self.duration = duration
        self.volume = volume
        self.octave = octave

    def play(self, midi_out):
        # Executa a nota usando o canal MIDI 
        # Pitch Final = Pitch Base + (12 * oitava)
        midi_out.note_on(self.pitch + (self.octave * 12), self.volume) 
        pygame.time.delay(int(self.duration * 1000))
        midi_out.note_off(self.pitch + (self.octave * 12), self.volume)
        self.pitch = self.pitch + (self.octave * 12) #Nota tocada de fato
