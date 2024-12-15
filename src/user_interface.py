import customtkinter as ctk
from tkinter import filedialog, messagebox
from src.music_generator import MusicGenerator


class MusicAppUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("Gerador Musical")
        self.geometry("800x600")

        # Inicializa o gerador de música
        self.generator = MusicGenerator()

        # Configurações iniciais
        self.initial_volume = self.generator.volume
        self.initial_octave = self.generator.octave
        self.initial_bpm = self.generator.duration * 60
        self.initial_instrument = "Piano"
        self.instrument_options = {
            "Piano": 0,
            "Xilofone": 14,
            "Tubular Bells": 15,
            "Órgão": 19
        }

        # Layout principal: Dividido em dois frames
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.left_frame = ctk.CTkFrame(self.main_frame, width=400)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=10)

        self.right_frame = ctk.CTkFrame(self.main_frame, width=300)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10)

        # Configuração das Seções
        self.setup_left_frame()
        self.setup_right_frame()

    def setup_left_frame(self):
        # Campo de texto e botões à esquerda
        label = ctk.CTkLabel(self.left_frame, text="Digite o texto ou carregue de um arquivo:")
        label.pack(pady=10)

        self.text_input = ctk.CTkTextbox(self.left_frame, height=300, width=350)
        self.text_input.pack(pady=10)

        loadFile_button = ctk.CTkButton(self.left_frame, text="Carregar Arquivo", command=self.load_file)
        loadFile_button.pack(pady=10)

        # Botão para salvar o arquivo MIDI
        save_button = ctk.CTkButton(self.left_frame, text="Salvar como MIDI", command=self.save_midi)
        save_button.pack(pady=10)

        generateMusic_button = ctk.CTkButton(self.left_frame, text="Gerar Música", command=self.generate_music)
        generateMusic_button.pack(pady=10)

    def setup_right_frame(self):
        # Configurações de Volume, Oitava e Instrumento à direita
        config_label = ctk.CTkLabel(self.right_frame, text="Configurações Iniciais", font=("Arial", 16))
        config_label.pack(pady=10)

        # Slider de volume
        volume_label = ctk.CTkLabel(self.right_frame, text=f"Volume Inicial: {self.initial_volume}")
        volume_label.pack(pady=10)

        self.volume_slider = ctk.CTkSlider(self.right_frame, from_=0, to=127, command=lambda value: volume_label.configure(text=f"Volume Inicial: {int(value)}"))
        self.volume_slider.set(self.initial_volume)
        self.volume_slider.pack(pady=10)

        # Opções de oitava
        octave_label = ctk.CTkLabel(self.right_frame, text="Oitava Inicial:")
        octave_label.pack(pady=10)

        self.octave_dropdown = ctk.CTkOptionMenu(self.right_frame, values=[str(i) for i in range(0, 9)])
        self.octave_dropdown.set(str(self.initial_octave))
        self.octave_dropdown.pack(pady=10)

        # Slider de BPM
        bpm_label = ctk.CTkLabel(self.right_frame, text=f"BPM Inicial: {self.initial_bpm}")
        bpm_label.pack(pady=10)

        self.bpm_slider = ctk.CTkSlider(self.right_frame, from_=0, to=60, command=lambda value: bpm_label.configure(text=f"BPM Inicial: {int(value)}"))
        self.bpm_slider.set(self.initial_bpm)
        self.bpm_slider.pack(pady=10)

        # Opções de instrumento
        instrument_label = ctk.CTkLabel(self.right_frame, text="Instrumento Inicial:")
        instrument_label.pack(pady=10)

        self.instrument_dropdown = ctk.CTkOptionMenu(self.right_frame, values=list(self.instrument_options.keys()))
        self.instrument_dropdown.set(self.initial_instrument)
        self.instrument_dropdown.pack(pady=10)

        # Botão para aplicar configurações
        apply_button = ctk.CTkButton(self.right_frame, text="Aplicar Configurações", command=self.apply_settings)
        apply_button.pack(pady=20)

    def load_file(self):
        file_path = filedialog.askopenfilename(title="Selecione um Arquivo", filetypes=[("Arquivos de Texto", "*.txt")])
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.text_input.delete("0.0", "end")
                    self.text_input.insert("0.0", file.read())
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar arquivo: {e}")
    
    #Não ta funcionado
    def save_midi(self):
        # Abre o diálogo para escolher o local de salvamento
        file_path = filedialog.asksaveasfilename(
            title="Salvar Arquivo MIDI",
            defaultextension=".midi",
            filetypes=[("Arquivo MIDI", "*.midi")]
        )

        # Salva o arquivo MIDI
        self.generator.save_midi(file_path)
        messagebox.showinfo("Arquivo Salvo", f"Arquivo MIDI salvo em: {file_path}")
    

    def apply_settings(self):
        self.initial_volume = int(self.volume_slider.get())
        self.initial_octave = int(self.octave_dropdown.get())
        self.initial_bpm = int(self.bpm_slider.get())
        self.initial_instrument = self.instrument_dropdown.get()

        # Configura no gerador musical
        self.generator.volume = self.initial_volume
        self.generator.octave = self.initial_octave
        self.generator.duration = self.initial_bpm / 60
        self.generator.current_instrument.midi_code = self.instrument_options[self.initial_instrument]
        messagebox.showinfo("Configurações", "Configurações aplicadas com sucesso!")

    def generate_music(self):
        text = self.text_input.get("0.0", "end").strip()
        if not text:
            messagebox.showwarning("Entrada Vazia", "Por favor, insira um texto para gerar a música!")
        else:
            self.generator.generate_music(text)
            messagebox.showinfo("Música Gerada", "A música foi gerada com sucesso!")
        self.generator.volume = self.initial_volume
        self.generator.octave = self.initial_octave
        self.generator.duration = self.initial_bpm / 60
        self.generator.current_instrument.midi_code = self.instrument_options[self.initial_instrument]
