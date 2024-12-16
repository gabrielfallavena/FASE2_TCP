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
        self.current_instrument = Instrument("Piano")
        self.mapper = CharacterMapper()
        self.midi_out = pygame.midi.Output(0)        

        self.midi_file = MidiFile() 
        self.track = MidiTrack()     
        self.midi_file.tracks.append(self.track)  

        self.track.append(Message('program_change', program=0, time=0))

    def generate_music(self, input_text):
        for char in input_text:
            action, value, text = self.mapper.map_character(char)
            match action:
                case 'note':
                    self.play_note(value)
                case 'volume':
                    if(value == 'up'):
                        self.add_volume()
                    elif(value == 'down'):
                        self.dec_volume()
                    elif(value == 'max'):
                        self.max_volume()
                    else:
                        self.min_volume()
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
                    self.pause(value)

    def play_note(self, pitch_base):
        # Calcula o valor final do pitch somando a base com a oitava
        note = Note(pitch_base, self.duration, self.volume, self.octave)
        note.play(self.midi_out)

    def add_volume(self):
        self.volume = min(self.volume + 10 , 127) 

    def dec_volume(self):
        self.volume = max(self.volume - 10, 0) 
    
    def max_volume(self):
        self.volume = 127
    
    def min_volume(self):
        self.volume = 5

    def switch_midi_out(self, instrument):
        # Troca o instrumento atual e o midi_out para o instrumento passado
        instrument = Instrument(instrument)
        self.current_instrument = instrument
        self.midi_out.set_instrument(self.current_instrument.midi_code)

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

    def pause(self, pause_duration):
        # Pausa entre ações de acordo com o valor passado
        pygame.time.delay(pause_duration)

    #def save_midi(self, file_path):
        # Salva o arquivo MIDI gerado
    #    self.midi_file.save(file_path)
    #    print(f"Arquivo MIDI salvo em: {file_path}")
