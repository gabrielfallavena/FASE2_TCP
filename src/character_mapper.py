# Mapeia os caracteres para as suas ações correspondentes 
class CharacterMapper:
    def __init__(self):
        self.character_map = {}
        self.initialize_mapping()

    def initialize_mapping(self):
        self.character_map = {
            'A': ('note', 21),  # Nota Lá na oitava 0
            'B': ('note', 23),  # Nota Si na oitava 0
            'C': ('note', 12),  # Nota Dó na oitava 0
            'D': ('note', 14),  # Nota Ré na oitava 0
            'E': ('note', 16),  # Nota Mi na oitava 0
            'F': ('note', 17),  # Nota Fá na oitava 0
            'G': ('note', 19),  # Nota Sol na oitava 0
            ' ': ('volume', None),    # Ajuste de volume
            '+': ('duration', 'up'),  # Sobe o bpm
            '-': ('duration', 'down'),  # Desce o bpm
            '?': ('octave', 'up'),    # Sobe uma oitava
            '.': ('octave', 'up'),    # Sobe uma oitava
            '$': ('octave', 'down'),  # Sobe uma oitava
            '!': ('instrument', 14),  # Troca para Xilofone
            '\n': ('instrument', 15), # Troca para Tubular Bells
            ';': ('instrument', 126), # Troca para Helicoptero
            ',': ('instrument', 105),  # Troca para Citara
            '%': ('instrument', 2)  # Troca para Piano
            
        }

    def map_character(self, char):
        # Retorna o mapeamento do caractere ou uma pausa como padrão
        return self.character_map.get(char, ('pause', None))

