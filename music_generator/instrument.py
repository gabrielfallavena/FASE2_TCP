class Instrument:
    def __init__(self, name, midi_code):
        self.name = name
        self.midi_code = midi_code

    def switch_to(self, midi_out):
        # Troca o instrumento MIDI
        midi_out.set_instrument(self.midi_code)
