# Classe principal de funcionamento do Music Generator
# Possui os atributos como volume, oitava e instrumentos atuais, 
# além dos métodos necessários para alterá-los

import pygame.midi
from src.character_mapper import CharacterMapper
from src.instrument import Instrument
from src.note import Note
from mido import MidiFile, MidiTrack, Message

PPQ = 960
MAX_OCTAVE = 8
MIN_OCTAVE = 0
MAX_VOLUME = 127
MIN_VOLUME = 0
VAR_VOLUME = 10
VAR_DURATION = 4
INITIAL_VOLUME = 32
INITIAL_OCTAVE = 4
INITIAL_DURATION = 30
INITIAL_INSTRUMENT = Instrument("Piano")

class MusicGenerator:
    def __init__(self):
        self.volume = INITIAL_VOLUME 
        self.octave = INITIAL_OCTAVE
        self.duration = INITIAL_DURATION
        self.current_instrument = INITIAL_INSTRUMENT
        self.mapper = CharacterMapper()
        self.midi_out = pygame.midi.Output(0)        

        self.midi_file = MidiFile() 
        self.track = MidiTrack()     
        self.midi_file.tracks.append(self.track)  

        self.track.append(Message('program_change', program=0, time=0))

    def generate_music(self, input_text):
        self.clear_track()
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
                case _:
                    print(text)
                    self.pause(1)    

    def play_note(self, pitch_base):
        # Calcula o valor final do pitch somando a base com a oitava
        note = Note(pitch_base, self.duration/60, self.volume, self.octave)
        note.play(self.midi_out)
        self.track.append(Message('note_on', note=note.pitch, velocity=self.volume, time=0))  
        self.track.append(Message('note_off', note=note.pitch, velocity=self.volume, time=int(PPQ*self.duration/60))) 

    def add_volume(self):
        self.volume = min(self.volume + VAR_VOLUME , MAX_VOLUME) 

    def dec_volume(self):
        self.volume = max(self.volume - VAR_VOLUME, MIN_VOLUME) 
    
    def max_volume(self):
        self.volume = MAX_VOLUME
    
    def min_volume(self):
        self.volume = MIN_VOLUME

    def switch_midi_out(self, instrument):
        # Troca o instrumento atual e o midi_out para o instrumento passado
        instrument = Instrument(instrument)
        self.current_instrument = instrument
        self.midi_out.set_instrument(self.current_instrument.midi_code)

    def add_octave(self):
        # Sobe uma oitava dentro dos limites do MIDI
        self.octave = min(self.octave + 1, MAX_OCTAVE)

    def dec_octave(self):
        # Desce uma oitava dentro dos limites do MIDI
        self.octave = max(self.octave - 1, MIN_OCTAVE)

    def add_duration(self):
        # Aumenta a duração da nota
        self.duration += VAR_DURATION

    def dec_duration(self):
        # Diminui a duração da nota (mínimo 0)
        self.duration = max(self.duration - VAR_DURATION, 1)

    def pause(self, pause_duration):
        # Pausa entre ações de acordo com o valor passado
        pygame.time.delay(pause_duration)
        self.track.append(Message('note_on', note=0, velocity=0, time=int(pause_duration*PPQ/1000))) # Para segundos 

    def save_midi(self, file_name):
        # Salva o arquivo MIDI gerado
        self.midi_file.save(file_name)
        print(f"Arquivo MIDI salvo como {file_name}")

    def clear_track(self):
        # Remove todos os eventos da faixa
        self.track = MidiTrack() 
        self.midi_file.tracks = [self.track]