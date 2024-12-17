# Classe própria do instrumento

class Instrument:

    # Dicionário de instrumentos MIDI
    ALL_INSTRUMENTS = {
        "Piano": 0,
        "Piano Elétrico": 6,
        "Xilofone": 14,
        "Tubular Bells": 15,
        "Órgão": 19,
        "Acordeão": 22,
        "Guitarra Elétrica": 30,
        "Baixo Elétrico": 34,
        "Violino": 40,
        "Voz Humana": 54,
        "Flauta": 73,
        "Ocarina": 80,
        "Helicóptero": 126
    }

    def __init__(self, name):
        if name not in Instrument.ALL_INSTRUMENTS:
            raise ValueError(f"Instrumento '{name}' não está disponível")
        self.name = name
        self.midi_code = Instrument.ALL_INSTRUMENTS[name]

    def switch_to(self, midi_out):
        # Troca o instrumento MIDI
        midi_out.set_instrument(self.midi_code)

    @classmethod
    def list_instruments(cls):
        # Retorna uma lista de todos os instrumentos disponíveis.
        return list(cls.ALL_INSTRUMENTS.keys())
