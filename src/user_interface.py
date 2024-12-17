import customtkinter as ctk
from tkinter import filedialog, messagebox
from src.music_generator import MusicGenerator
from src.instrument import Instrument
from src.character_mapper import CharacterMapper


class MusicAppUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("Gerador Musical")
        self.geometry("1000x600")

        # Inicializa o gerador de música
        self.generator = MusicGenerator()

        # Configurações iniciais
        self.initial_volume = self.generator.volume
        self.initial_octave = self.generator.octave
        self.initial_duration = self.generator.duration
        self.initial_instrument = self.generator.current_instrument.name

         # Layout principal (esquerda, centro e direita)
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.left_frame = ctk.CTkScrollableFrame(self.main_frame, width=220)
        self.left_frame.pack(side="left", fill="y", padx=10)

        self.center_frame = ctk.CTkFrame(self.main_frame, width=400)
        self.center_frame.pack(side="left", fill="both", expand=True, padx=10)

        self.right_frame = ctk.CTkFrame(self.main_frame, width=300)
        self.right_frame.pack(side="right", fill="y", padx=10)

        # Configuração das Seções
        self.setup_left_frame()
        self.setup_center_frame()
        self.setup_right_frame()

    def setup_left_frame(self):
        # Seção para mostrar os caracteres mapeados em formato de tabela.
        label = ctk.CTkLabel(self.left_frame, text="Mapeamento de Caracteres", font=("Arial", 16, "bold"))
        label.grid(row=0, column=0, columnspan=2, pady=10)  # Coloca o título no topo

        char_mapper = CharacterMapper() 
        mapping = char_mapper.get_mapping()  # Obtém o mapeamento de caracteres

        # Títulos das colunas
        char_title = ctk.CTkLabel(self.left_frame, text="Caractere", font=("Arial", 12, "bold"))
        action_title = ctk.CTkLabel(self.left_frame, text="Ação", font=("Arial", 12, "bold"))
        char_title.grid(row=1, column=0, padx=5, pady=5)
        action_title.grid(row=1, column=1, padx=5, pady=5)

        # Preenchendo a tabela com o mapeamento
        row = 2 
        for char, action in mapping.items():
            char_label = ctk.CTkLabel(self.left_frame, text=char, font=("Arial", 12))
            action_label = ctk.CTkLabel(self.left_frame, text=f"{action[2]}", font=("Arial", 12))
            char_label.grid(row=row, column=0, padx=2, pady=0)
            action_label.grid(row=row, column=1, padx=2, pady=0)
            row += 1 

    def setup_center_frame(self):
        # Campo de texto e botões à esquerda
        label = ctk.CTkLabel(self.center_frame, text="Digite o texto ou carregue de um arquivo:", font=("Arial", 16, "bold"))
        label.pack(pady=10)

        self.text_input = ctk.CTkTextbox(self.center_frame, height=300, width=400)
        self.text_input.pack(pady=10)

        loadFile_button = ctk.CTkButton(self.center_frame, text="Carregar Arquivo", command=self.load_file)
        loadFile_button.pack(pady=10)

        # Botão para salvar o arquivo MIDI
        save_button = ctk.CTkButton(self.center_frame, text="Salvar como MIDI", command=self.save_midi)
        save_button.pack(pady=10)

        generateMusic_button = ctk.CTkButton(self.center_frame, text="Gerar Música", command=self.generate_music)
        generateMusic_button.pack(pady=10)

    def setup_right_frame(self):
        # Configurações de Volume, Oitava e Instrumento à direita
        config_label = ctk.CTkLabel(self.right_frame, text="Configurações Iniciais", font=("Arial", 16, "bold"))
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

        # Slider de Duração
        duration_label = ctk.CTkLabel(self.right_frame, text=f"Duração Inicial: {self.initial_duration}")
        duration_label.pack(pady=10)

        self.duration_slider = ctk.CTkSlider(self.right_frame, from_=1, to=60, command=lambda value: duration_label.configure(text=f"Duração Inicial: {int(value)}"))
        self.duration_slider.set(self.initial_duration)
        self.duration_slider.pack(pady=10)

        # Opções de instrumento
        instrument_label = ctk.CTkLabel(self.right_frame, text="Instrumento Inicial:")
        instrument_label.pack(pady=10)

        # Obtem os instrumentos disponíveis diretamente da classe `Instrument`
        instrument_list = Instrument.list_instruments()
        self.instrument_dropdown = ctk.CTkOptionMenu(self.right_frame, values=instrument_list)
        self.instrument_dropdown.set(self.initial_instrument)  # Define o valor inicial
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
        self.initial_duration = int(self.duration_slider.get())
        self.initial_instrument = self.instrument_dropdown.get()

        # Configura no gerador musical
        self.generator.volume = self.initial_volume
        self.generator.octave = self.initial_octave
        self.generator.duration = self.initial_duration
        self.generator.switch_midi_out(self.initial_instrument)
        messagebox.showinfo("Configurações", "Configurações aplicadas com sucesso!")

    def generate_music(self):
        text = self.text_input.get("0.0", "end").strip()
        if not text:
            messagebox.showwarning("Entrada Vazia", "Por favor, insira um texto para gerar a música!")
        else:
            self.generator.generate_music(text)
            messagebox.showinfo("Música Gerada", "A música foi gerada com sucesso!")

        # Reload das configurações iniciais 
        self.generator.volume = self.initial_volume
        self.generator.octave = self.initial_octave
        self.generator.duration = self.initial_duration
        self.generator.switch_midi_out(self.initial_instrument)