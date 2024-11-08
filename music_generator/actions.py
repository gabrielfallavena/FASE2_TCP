# Contém as ações possíveis de se realizar

from enum import Enum

# Enum ActionType
class ActionType(Enum):
    PLAY_NOTE = "play_note"
    CHANGE_VOLUME = "change_volume"
    SWITCH_INSTRUMENT = "switch_instrument"
    CHANGE_OCTAVE = "change_octave"
    PAUSE = "pause"

# Classe MusicAction
class MusicAction:
    def __init__(self, action_type, value=None):
        self.action_type = action_type
        self.value = value

    def execute(self, generator):
        # Executa a ação com base no tipo
        if self.action_type == ActionType.PLAY_NOTE:
            generator.play_note(self.value)
        elif self.action_type == ActionType.CHANGE_VOLUME:
            generator.adjust_volume(self.value)
        elif self.action_type == ActionType.SWITCH_INSTRUMENT:
            generator.switch_instrument(self.value)
        elif self.action_type == ActionType.CHANGE_OCTAVE:
            generator.change_octave(self.value)
        elif self.action_type == ActionType.PAUSE:
            generator.pause()
