# Classe principal de funcionamento do Music Generator
# Possui os atributos como volume, oitava e instrumentos atuais, 
# além dos métodos necessários para alterá-los

import pygame.midi
from src.character_mapper import CharacterMapper
from src.instrument import Instrument
from src.note import Note
from mido import MidiFile, MidiTrack, Message

class MusicGenerator:
    def __init__(self):
        self.volume = 32
        self.octave = 4
        self.duration = 0.5
        self.current_instrument = Instrument("Piano", 0)
        self.mapper = CharacterMapper()
        self.midi_out = pygame.midi.Output(0)
        self.current_instrument.switch_to(self.midi_out)
        

        self.midi_file = MidiFile() 
        self.track = MidiTrack()     
        self.midi_file.tracks.append(self.track)  

        self.track.append(Message('program_change', program=0, time=0))

    def generate_music(self, text):
        for char in text:
            action, value = self.mapper.map_character(char)
            match action:
                case 'note':
                    self.play_note(value)
                    #self.track.append(Message('note_on', note= value + 12*self.octave, velocity=self.volume, time=0))
                    #self.track.append(Message('note_off', note= value + 12*self.octave, velocity=self.volume, time=self.duration))  # Duração da nota
                case 'volume':
                    self.adjust_volume()
                case 'instrument':
                    self.switch_instrument(value)
                case 'octave':
                    if(value == 'up'):
                        self.add_octave()
                    else:
                        self.dec_octave()
                case 'duration':
                    if(value == 'up'):
                        self.add_duration()
                    else:
                        self.dec_duration()
                case 'pause':
                    self.pause()

    def play_note(self, pitch_base):
        # Calcula o valor final do pitch somando a base com a oitava
        note = Note(pitch_base, self.duration, self.volume, self.octave)
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

    def dec_octave(self):
        # Desce uma oitava dentro dos limites do MIDI
        self.octave = max(self.octave - 1, 0)

    def add_duration(self):
        # Aumenta a duração da nota
        self.duration += 0.1

    def dec_duration(self):
        # Diminui a duração da nota
        self.duration -= 0.1

    def pause(self):
        # Pausa entre ações
        pygame.time.delay(100)

    #def save_midi(self, file_path):
        # Salva o arquivo MIDI gerado
    #    self.midi_file.save(file_path)
    #    print(f"Arquivo MIDI salvo em: {file_path}")
