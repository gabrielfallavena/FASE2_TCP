# Mapeia os caracteres para as suas ações correspondentes 

from .actions import MusicAction, ActionType

class CharacterMapper:
    def __init__(self):
        self.character_map = {}
        self.initialize_mapping()

    def initialize_mapping(self):
        # Mapeamento das notas 
        self.character_map['A'] = MusicAction(ActionType.PLAY_NOTE, 69)  # Nota Lá
        self.character_map['B'] = MusicAction(ActionType.PLAY_NOTE, 71)  # Nota Si
        self.character_map['C'] = MusicAction(ActionType.PLAY_NOTE, 60)  # Nota Dó
        self.character_map['D'] = MusicAction(ActionType.PLAY_NOTE, 62)  # Nota Ré
        self.character_map['E'] = MusicAction(ActionType.PLAY_NOTE, 64)  # Nota Mi
        self.character_map['F'] = MusicAction(ActionType.PLAY_NOTE, 65)  # Nota Fá
        self.character_map['G'] = MusicAction(ActionType.PLAY_NOTE, 67)  # Nota Sol
        
        #ADICIONAR CARACTERES RESTANTES

    def map_character(self, char):
        # Retorna a ação correspondente ao caractere
        return self.character_map.get(char, MusicAction(ActionType.PAUSE))
