import tkinter as tk
import tkintermapview
from menu_lateral import Menu_lateral

class Telas:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x800")
        self.root.configure(bg="#B0E0E6")

        self.menu = Menu_lateral(
            self.root,
            comando_ir_mapa=lambda: self.mostrar_tela(Mapa_tela),
            comando_ir_inicio=lambda: self.mostrar_tela(Equipe),
            comando_ir_dados=lambda: self.mostrar_tela(Dados),
            comando_ir_relatorios=lambda: self.mostrar_tela(Relatorio)
        )

        self.area_principal = tk.Frame(self.root)
        self.area_principal.pack(side="right", fill="both", expand=True)

        self.frames = {}

        for ClasseTela in (Mapa_tela, Equipe, Dados, Relatorio):

            frame = tk.Frame(self.area_principal)
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

            ClasseTela(frame)
            self.frames[ClasseTela] = frame

        self.mostrar_tela(Mapa_tela)

    def mostrar_tela(self, tela_desejada):
        frame = self.frames[tela_desejada]
        frame.tkraise()

class Mapa_tela:

    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#B0E0E6")
        self.tela() 

        self.start_x = None
        self.start_y = None
        self.rect_id = None

    def get_cords(self):
        lat_text = self.set_lat.get()
        lon_text = self.set_long.get()

        try:
            lat = float(lat_text)
            long = float(lon_text)

            self.map_widget.set_position(lat, long)
            self.map_widget.set_zoom(12)
            # map_widget.set_marker(lat, long, text="Nova posição")
        except ValueError:
            print("Por favor, digite apenas números válidos")

    def tela(self):
        self.frame_lateral = tk.LabelFrame(self.root, width=250, bg="#ADD8E6")
        self.frame_lateral.pack(side="right", fill="y", pady=(20, 15), padx=(0,20))
        self.frame_lateral.pack_propagate(False)

        self.frame_text = tk.Frame(self.frame_lateral, bg="#ADD8E6")
        self.frame_text.pack(expand=True)

        #-------------------------------------------------
        tk.Label(self.frame_text, text="Latitude 1:", bg="#ADD8E6", font=("Arial", 9, "bold")).pack(pady=(0,2))
        self.set_lat1 = tk.Entry(self.frame_text, justify="center")
        self.set_lat1.pack( pady=(0,5))

        tk.Label(self.frame_text, text="Longitude 1:", bg="#ADD8E6", font=("Arial", 9, "bold")).pack(pady=(0,2))
        self.set_lon1 = tk.Entry(self.frame_text, justify="center")
        self.set_lon1.pack( pady=(0,5))

        tk.Label(self.frame_text, text="Latitude 2:", bg="#ADD8E6", font=("Arial", 9, "bold")).pack(pady=(0,2))
        self.set_lat2 = tk.Entry(self.frame_text, justify="center")
        self.set_lat2.pack( pady=(0,5))

        tk.Label(self.frame_text, text="Longitude 2:", bg="#ADD8E6", font=("Arial", 9, "bold")).pack(pady=(0,2))
        self.set_lon2 = tk.Entry(self.frame_text, justify="center")
        self.set_lon2.pack( pady=(0,10))

        self.button_marcar = tk.Button(self.frame_text, text="Selecionar Região", command=self.capturar_entradas_e_desenhar)
        self.button_marcar.pack(pady=(0,10))

        self.button_remove = tk.Button(self.frame_text, text="Apagar marcação", command=self.limpar_marcacao)
        self.button_remove.pack(pady=(0,100))

        #-------------------------------------------------

        # self.button_area = tk.Button(self.frame_text, text="Selecionar Area", command=self.ativar_selecao)
        # self.button_area.pack(pady=(0,50))

        # Entradas de Texto
        tk.Label(self.frame_text, text="Latitude:", bg="#ADD8E6", font=("Arial", 9, "bold")).pack(pady=(0,2))
        self.set_lat = tk.Entry(self.frame_text, justify="center")
        self.set_lat.pack( pady=(0,5))

        tk.Label(self.frame_text, text="Longitude:", bg="#ADD8E6", font=("Arial", 9, "bold")).pack(pady=(0,2))
        self.set_long = tk.Entry(self.frame_text, justify="center")
        self.set_long.pack(pady=(0,5))

        # Botão
        self.button_search = tk.Button(self.frame_text, text="Buscar Coordenadas", command=self.get_cords)
        self.button_search.pack()

        # --- Mapa ---
        self.map_label = tk.LabelFrame(self.root, width=250)
        self.map_label.pack(padx=(20,20), pady=(20, 15), side="left", fill="both", expand=True)

        self.map_widget = tkintermapview.TkinterMapView(self.map_label, width=1000, height=800)
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=y&hl=pt-BR&x={x}&y={y}&z={z}&s=Ga")
        self.map_widget.set_position(-28.9510156, -49.4678388) # Posição inicial (UFSC-Ararangua)
        self.map_widget.set_zoom(18)
        self.map_widget.pack(fill="both",expand=True)

    def desenhar_regiao_geografica(self, lat1, lon1, lat2, lon2):
        
        if hasattr(self, 'poligono_selecao') and self.poligono_selecao:
            self.poligono_selecao.delete()

        ponto_superior_esquerdo = (lat1, lon1)
        ponto_superior_direito  = (lat1, lon2)
        ponto_inferior_direito  = (lat2, lon2)
        ponto_inferior_esquerdo = (lat2, lon1)

        caminho_quadrado = [
            ponto_superior_esquerdo, 
            ponto_superior_direito, 
            ponto_inferior_direito, 
            ponto_inferior_esquerdo
        ]

        self.poligono_selecao = self.map_widget.set_polygon(
            caminho_quadrado,
            fill_color=None,             # Sem preenchimento interno (transparente)
            outline_color="red",         # Cor da borda do quadrado
            border_width=3,              # Espessura da linha
            name="regiao_marcada"
        )

    def capturar_entradas_e_desenhar(self):
        try:
            lat1 = float(self.set_lat1.get())
            lon1 = float(self.set_lon1.get())
            lat2 = float(self.set_lat2.get())
            lon2 = float(self.set_lon2.get())

            self.desenhar_regiao_geografica(lat1, lon1, lat2, lon2)
            
        except ValueError:
            print("Erro de digitação: Certifique-se de preencher todos os campos apenas com números e usar ponto (ex: -27.59) em vez de vírgula.")

    def limpar_marcacao(self):

        if hasattr(self, 'poligono_selecao') and self.poligono_selecao:
            self.poligono_selecao.delete()
            self.poligono_selecao = None

        if hasattr(self, 'rect_id') and self.rect_id:
            self.map_widget.canvas.delete(self.rect_id)
            self.rect_id = None

        self.set_lat1.delete(0, tk.END)
        self.set_lon1.delete(0, tk.END)
        self.set_lat2.delete(0, tk.END)
        self.set_lon2.delete(0, tk.END)
        
        print("Marcação e coordenadas apagadas com sucesso.")

class Dados:

    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#B0E0E6")
        self.tela_dado() 

    def tela_dado(self):

        self.img_label = tk.LabelFrame(self.root, width=250)
        self.img_label.pack(padx=(20,20), pady=(20, 15), side="left", fill="both", expand=True)
    
        #----------------------------------
        self.frame_dado = tk.LabelFrame(self.root, width=250, bg="white")
        self.frame_dado.pack(side="right", fill="y", pady=(20, 15), padx=(0,20))
        self.frame_dado.pack_propagate(False)
               

class Relatorio:  

    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#B0E0E6")
        self.tela_relatorio() 

    def tela_relatorio(self):

        self.relatorio_label = tk.LabelFrame(self.root, width=250)
        self.relatorio_label.pack(padx=(20,20), pady=(20, 15), side="left", fill="both", expand=True) 

        self.frame_relatorio = tk.LabelFrame(self.root, width=250, bg="green")
        self.frame_relatorio.pack(side="right", fill="y", pady=(20, 15), padx=(0,20))
        self.frame_relatorio.pack_propagate(False)       

class Equipe:
    def __init__(self, parent):
        self.parent = parent
        self.parent.configure(bg="#B0E0E6")
        
        self.tela()

    def tela(self):
       
        self.frame_principal = tk.Frame(self.parent, bg="white")
        self.frame_principal.pack(expand=True, fill="both", padx=20, pady=20)