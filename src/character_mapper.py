# Mapeia os caracteres para as suas ações correspondentes 
class CharacterMapper:
    def __init__(self):
        self.character_map = {}
        self.initialize_mapping()

    def initialize_mapping(self):
        self.character_map = {
            'C': ('note', 12, 'C0'),          # Nota Dó na oitava 0 = C0
            'c': ('note', 13, 'C#0'),          # Nota Dó sustenido na oitava 0 = C#0
            'D': ('note', 14, 'D0'),          # Nota Ré na oitava 0 = D0
            'd': ('note', 15, 'D#0'),          # Nota Ré sustenido na oitava 0 = D#0
            'E': ('note', 16, 'E0'),          # Nota Mi na oitava 0 = E0
            'F': ('note', 17, 'F0'),          # Nota Fá na oitava 0 = F0
            'f': ('note', 18, 'F#0'),          # Nota Fá sustenido na oitava 0 = F#0
            'G': ('note', 19, 'G'),          # Nota Sol na oitava 0 = G0
            'g': ('note', 20, 'G#0'),          # Nota Sol sustenido na oitava 0 = G#0 
            'A': ('note', 21, 'A0'),          # Nota Lá na oitava 0 = A0
            'a': ('note', 22, 'A#0'),          # Nota Lá sustenido na oitava 0 = A#0
            'B': ('note', 23, 'B0'),          # Nota Si na oitava 0 = B0
            'V': ('volume', 'up', 'Volume Up'),      # Aumenta volume
            'v': ('volume', 'down', 'Volume down'),    # Diminui volume
            'M': ('volume', 'max', 'Max Volume'),     # Aumenta volume
            'm': ('volume', 'min', 'Min Volume'),     # Diminui volume
            '+': ('duration', 'up', 'Inc BPM'),    # Sobe o bpm
            '-': ('duration', 'down', 'Dec BPM'),  # Desce o bpm
            '>': ('octave', 'up', 'Inc Octave'),      # Sobe uma oitava
            '<': ('octave', 'down', 'Dec Octave'),    # Sobe uma oitava
            'S': ('pause', 100, 'Pause 100 ms'),        # Pause por 100 ms
            'H': ('pause', 250, 'Pause 250 ms'),        # Pause por 250 ms
            'L': ('pause', 500, 'Pause 500 ms'),        # Pause por 500 ms
            'X': ('pause', 1000, 'Pause 1000 ms'),       # Pause por 1000 ms

        }
    
    def get_mapping(self):
        return self.character_map

    def map_character(self, char):
        # Retorna o mapeamento do caractere ou uma pausa por 100 ms como padrão
        return self.character_map.get(char, ('pause', 100))

