import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from src.music_generator import MusicGenerator  # Importa o gerador musical

class MusicAppUI:
    def __init__(self, root):
        self.generator = MusicGenerator()

        # Configurações iniciais
        self.initial_volume = 64
        self.initial_octave = 4
        self.initial_instrument = 0

        # Configura a janela principal
        self.root = root
        self.root.title("Gerador Musical")

        # Layout principal (dois frames: esquerda e direita)
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.left_frame = tk.Frame(self.main_frame, padx=10, pady=10)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.right_frame = tk.Frame(self.main_frame, padx=10, pady=10)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Seção Esquerda: Entrada de Texto e Geração de Música
        self.setup_left_frame()

        # Seção Direita: Configurações de Volume, Oitava e Instrumento
        self.setup_right_frame()

    def setup_left_frame(self):
        # Texto explicativo
        label = tk.Label(self.left_frame, text="Digite o texto ou carregue de um arquivo:")
        label.pack(pady=10)

        # Campo de entrada para o texto
        self.text_input = tk.Text(self.left_frame, height=15, width=40)
        self.text_input.pack(pady=10)

        # Botão para carregar arquivo
        load_button = tk.Button(self.left_frame, text="Carregar Arquivo", command=self.load_file)
        load_button.pack(pady=5)

        # Botão para gerar a música
        generate_button = tk.Button(self.left_frame, text="Gerar Música", command=self.generate_music)
        generate_button.pack(pady=10)

    def setup_right_frame(self):
        # Título das configurações
        config_label = tk.Label(self.right_frame, text="Configurações Iniciais")
        config_label.pack(pady=10)

        # Volume inicial
        volume_label = tk.Label(self.right_frame, text="Volume Inicial:")
        volume_label.pack(pady=5)
        self.volume_slider = tk.Scale(self.right_frame, from_=0, to=127, orient=tk.HORIZONTAL)
        self.volume_slider.set(self.initial_volume)
        self.volume_slider.pack(pady=5)

        # Oitava inicial
        octave_label = tk.Label(self.right_frame, text="Oitava Inicial:")
        octave_label.pack(pady=5)
        self.octave_dropdown = ttk.Combobox(self.right_frame, values=list(range(0, 9)), state="readonly")
        self.octave_dropdown.set(self.initial_octave)
        self.octave_dropdown.pack(pady=5)

        # Instrumento inicial
        instrument_label = tk.Label(self.right_frame, text="Instrumento Inicial:")
        instrument_label.pack(pady=5)
        instrument_options = {
            "Piano": 0,
            "Xilofone": 14,
            "Tubular Bells": 15,
            "Órgão": 19
        }
        self.instrument_dropdown = ttk.Combobox(self.right_frame, values=list(instrument_options.keys()), state="readonly")
        self.instrument_dropdown.set("Piano")
        self.instrument_options = instrument_options
        self.instrument_dropdown.pack(pady=5)

        # Botão para aplicar as configurações iniciais
        apply_button = tk.Button(self.right_frame, text="Aplicar Configurações", command=self.apply_settings)
        apply_button.pack(pady=10)

    def load_file(self):
        # Abre um diálogo para selecionar o arquivo
        file_path = filedialog.askopenfilename(
            title="Selecione um Arquivo",
            filetypes=[("Arquivos de Texto", "*.txt")]
        )
        if file_path:
            try:
                # Lê o conteúdo do arquivo e insere no campo de texto
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.text_input.delete("1.0", tk.END)  # Limpa o campo de texto
                    self.text_input.insert(tk.END, content)  # Insere o conteúdo
                messagebox.showinfo("Arquivo Carregado", f"Conteúdo carregado de: {file_path}")
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível carregar o arquivo.\nErro: {str(e)}")

    def apply_settings(self):
        # Atualiza as configurações iniciais do gerador
        self.initial_volume = self.volume_slider.get()
        self.initial_octave = int(self.octave_dropdown.get())
        self.initial_instrument = self.instrument_options[self.instrument_dropdown.get()]

        # Define no gerador musical
        self.generator.volume = self.initial_volume
        self.generator.octave = self.initial_octave
        self.generator.current_instrument.midi_code = self.initial_instrument
        self.generator.current_instrument.switch_to(self.generator.midi_out)

        messagebox.showinfo("Configurações Aplicadas", "As configurações iniciais foram atualizadas com sucesso!")

    def generate_music(self):
        # Recupera o texto inserido e gera a música
        input_text = self.text_input.get("1.0", tk.END).strip()
        
        if not input_text:
            messagebox.showwarning("Entrada Vazia", "Por favor, insira um texto para gerar a música!")
        else:
            self.generator.generate_music(input_text)
            messagebox.showinfo("Música Gerada", "A música foi gerada com sucesso!")
