import tkinter as tk
import tkintermapview

from tkinter import ttk, Scrollbar
from controller.C_shared import get_center
from controller.Functions import debug_print, get_map_image
from pathlib import Path
from PIL import Image, ImageTk
from model.databaseModel import get_search_by_term,get_all_history,get_result_by_id


class DetailView(tk.Toplevel):
    """A secondary window that accepts arguments."""

    def __init__(self, parent, slug):
        super().__init__(parent)
        self.title("Detalhes da Estimativa")
        self.geometry("833x558")
        self.configure(bg="#2C3E50") 
        self.data = {"ID":-1,"SLUG":"","TL_LAT":0.0, "TL_LON":0.0, "BR_LAT":0.0, "BR_LON":0.0, "CENT":0.0}

        # Painel Lateral
        self.frame_lateral = tk.Frame(self, width=280, bg="#2C3E50")
        self.frame_lateral.pack(side="right", fill="y", padx=(10, 20), pady=20)
        self.frame_lateral.pack_propagate(False)

        self.frame_text = tk.Frame(self.frame_lateral, bg="#2C3E50")
        self.frame_text.pack(expand=True, fill="both", padx=15, pady=15)
        
        search_data = get_search_by_term(slug)

        self.data["ID"],self.data["SLUG"],self.data["TL_LAT"],self.data["TL_LON"],self.data["BR_LAT"],self.data["BR_LON"] = search_data[0]

        center_lat,center_lon  = get_center(self.data["TL_LAT"],self.data["TL_LON"],self.data["BR_LAT"],self.data["BR_LON"])
        self.data["CENT"] = f"{center_lat}\n{center_lon}"
        debug_print("[id]")
        debug_print(self.data["ID"])

        specific_data = get_result_by_id(search_id=int(self.data["ID"]))
        debug_print("[pop, pop/km]")
        debug_print(specific_data)

        # Grupo: Coordenadas
        group_coords = tk.LabelFrame(self.frame_text, text=" Coordenadas da Área ", bg="#2C3E50", font=("Arial", 10, "bold"), fg="white")
        group_coords.pack(fill="x", pady=(0, 15))

        tk.Label(group_coords, text=f"Lat 1: {self.data['TL_LAT']}", anchor="w", justify="left", bg="#2C3E50", fg="white", font=("Arial", 9)).pack(fill="x", padx=5, pady=2)
        tk.Label(group_coords, text=f"Lon 1: {self.data['TL_LON']}", anchor="w", justify="left", bg="#2C3E50", fg="white", font=("Arial", 9)).pack(fill="x", padx=5, pady=2)
        tk.Label(group_coords, text=f"Lat 2: {self.data['BR_LAT']}", anchor="w", justify="left", bg="#2C3E50", fg="white", font=("Arial", 9)).pack(fill="x", padx=5, pady=2)
        tk.Label(group_coords, text=f"Lon 2: {self.data['BR_LON']}", anchor="w", justify="left", bg="#2C3E50", fg="white", font=("Arial", 9)).pack(fill="x", padx=5, pady=2)
        tk.Label(group_coords, text=f"Lat Centro: {center_lat}", anchor="w", justify="left", bg="#2C3E50", fg="white", font=("Arial", 9)).pack(fill="x", padx=5, pady=(5, 2))
        tk.Label(group_coords, text=f"Lon Centro: {center_lon}", anchor="w", justify="left", bg="#2C3E50", fg="white", font=("Arial", 9)).pack(fill="x", padx=5, pady=2)

        # Grupo: Resultados
        group_results = tk.LabelFrame(self.frame_text, text=" Resultados da Estimativa ", bg="#2C3E50", font=("Arial", 10, "bold"), fg="white")
        group_results.pack(fill="x", pady=10)

        tk.Label(group_results, text="População Estimada:", bg="#2C3E50", fg="white", font=("Arial", 9)).pack(pady=(10, 0))
        tk.Label(group_results, text=f"{specific_data[0]} Habitantes", bg="#2C3E50", fg="#4CAF50", font=("Arial", 10, "bold")).pack(pady=(0, 10))

        tk.Label(group_results, text="Densidade Aproximada:", bg="#2C3E50", fg="white", font=("Arial", 9)).pack(pady=(5, 0))
        tk.Label(group_results, text=f"{specific_data[1]}", bg="#2C3E50", fg="white", font=("Arial", 10, "bold")).pack(pady=(0, 10))

        # Imagem
        self.image_container = tk.LabelFrame(self, bg="#2C3E50", bd=0)
        self.image_container.pack(padx=(20, 10), pady=20, side="left", fill="both", expand=True)

        fp = f"media/processed/{slug}.png"
        img = Image.open(fp)
        self.rawphoto = ImageTk.PhotoImage(img)

        self.image= tk.Label(self.image_container, image=self.rawphoto, bg="#2C3E50")
        self.image.pack(expand=True)


class MainMapWindow(tk.Tk):
    def __init__(self):
        debug_print("setting up main window")
        super().__init__()
        self.title("Censo Demográfico via Satélite")
        self.geometry("1100x700") 
        self.configure(bg="#2C3E50")

        self.start_x = None
        self.start_y = None
        self.rect_id = None
        self.poligono_selecao = None
        self.selection_marker = None

        # --- Painel Lateral ---
        self.frame_lateral = tk.Frame(self, width=300, bg="#2C3E50")
        self.frame_lateral.pack(side="right", fill="y")
        self.frame_lateral.pack_propagate(False)

        # Container interno para aplicar padding
        self.panel_content = tk.Frame(self.frame_lateral, bg="#2C3E50")
        self.panel_content.pack(fill="both", expand=True, padx=20, pady=20)

        # 1. GRUPO: Seleção de Área 
        self.group_area = tk.LabelFrame(self.panel_content, text="Seleção de Área ", bg="#2C3E50", font=("Arial", 10, "bold"), fg="white")
        self.group_area.pack(fill="both", expand=True, pady=(0, 10))

        frame_coords = tk.Frame(self.group_area, bg="#2C3E50")
        frame_coords.pack(pady=(10, 5))

        tk.Label(frame_coords, text="Lat 1:", bg="#2C3E50", fg="white", font=("Arial", 9)).grid(row=0, column=0, sticky="e", pady=2, padx=2)
        self.set_lat1 = tk.Entry(frame_coords, width=12, justify="center")
        self.set_lat1.grid(row=0, column=1, pady=2, padx=2)

        tk.Label(frame_coords, text="Lon 1:", bg="#2C3E50", fg="white", font=("Arial", 9)).grid(row=0, column=2, sticky="e", pady=2, padx=2)
        self.set_lon1 = tk.Entry(frame_coords, width=12, justify="center")
        self.set_lon1.grid(row=0, column=3, pady=2, padx=2)

        tk.Label(frame_coords, text="Lat 2:", bg="#2C3E50", fg="white", font=("Arial", 9)).grid(row=1, column=0, sticky="e", pady=2, padx=2)
        self.set_lat2 = tk.Entry(frame_coords, width=12, justify="center")
        self.set_lat2.grid(row=1, column=1, pady=2, padx=2)

        tk.Label(frame_coords, text="Lon 2:", bg="#2C3E50", fg="white", font=("Arial", 9)).grid(row=1, column=2, sticky="e", pady=2, padx=2)
        self.set_lon2 = tk.Entry(frame_coords, width=12, justify="center")
        self.set_lon2.grid(row=1, column=3, pady=2, padx=2)

        # Botões da área de seleção
        self.button_remove = tk.Button(self.group_area, text="Apagar Marcação", cursor="hand2", fg="#D9534F", command=self.limpar_marcacao)
        self.button_remove.pack(fill="x", padx=15, pady=(0, 10))

        # Botão Pesquisar 
        self.button_confirm = tk.Button(self.group_area, text="Pesquisar Região", bg="#2196F3", fg="white", font=("Arial", 11, "bold"), cursor="hand2", command=self.search_selection)
        self.button_confirm.pack(fill="x", padx=15, ipady=8, pady=(0, 10))


        # 2. GRUPO: Navegação Rápida / Mover Mapa 
        self.group_nav = tk.LabelFrame(self.panel_content, text="Buscar no Mapa", bg="#2C3E50", font=("Arial", 10, "bold"), fg="white")
        self.group_nav.pack(fill="both", expand=True, pady=(10, 15))

        frame_nav = tk.Frame(self.group_nav, bg="#2C3E50")
        frame_nav.pack(pady=10)

        tk.Label(frame_nav, text="Lat:", bg="#2C3E50", fg="white", font=("Arial", 9)).grid(row=0, column=0, sticky="e", pady=2)
        self.set_lat = tk.Entry(frame_nav, width=15, justify="center")
        self.set_lat.grid(row=0, column=1, pady=2, padx=5)

        tk.Label(frame_nav, text="Lon:", bg="#2C3E50", fg="white", font=("Arial", 9)).grid(row=1, column=0, sticky="e", pady=2)
        self.set_long = tk.Entry(frame_nav, width=15, justify="center")
        self.set_long.grid(row=1, column=1, pady=2, padx=5)

        self.button_search = tk.Button(self.group_nav, text="Ir para Coordenada", cursor="hand2", command=self.get_cords)
        self.button_search.pack(fill="x", padx=15, pady=(5, 10))


        # 3. BOTÃO HISTÓRICO 
        self.button_relat = tk.Button(self.panel_content, text="Histórico / Relatório", bg="#2196F3", fg="white", font=("Arial", 11, "bold"), cursor="hand2", command=self.relatorio)
        self.button_relat.pack(fill="x", side="bottom", ipady=8)


        # --- Mapa ---
        self.map_frame = tk.Frame(self, bg="#2C3E50", bd=0)
        self.map_frame.pack(padx=(20, 10), pady=20, side="left", fill="both", expand=True)

        self.map_widget = tkintermapview.TkinterMapView(self.map_frame, corner_radius=0)
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=y&hl=pt-BR&x={x}&y={y}&z={z}&s=Ga")
        self.map_widget.set_position(-28.9510156, -49.4678388)  # Posição inicial (UFSC-Ararangua)
        self.map_widget.set_zoom(18)
        self.map_widget.pack(fill="both", expand=True)

        self.map_widget.add_right_click_menu_command(label="Selecionar Ponto 1 (Superior Esq.)",
                                                command=lambda coords: self.add_marker_event(coords,1),
                                                pass_coords=True)
        self.map_widget.add_right_click_menu_command(label="Selecionar Ponto 2 (Inferior Dir.)",
                                                command=lambda coords: self.add_marker_event(coords,2),
                                                pass_coords=True)

        debug_print("main window ready")

    def search_selection(self):
        debug_print("attempting to make new request")
        
        if not (self.set_lat1.get() and self.set_lon1.get() and self.set_lat2.get() and self.set_lon2.get()):
            print("Por favor, marque dois pontos no mapa ou digite as coordenadas antes de pesquisar.")
            return
        
        try:
            #Força a atualização do desenho no mapa com as coordenadas atuais das caixas de texto
            self.capturar_entradas_e_desenhar()

            lat1 = float(self.set_lat1.get())
            lon1 = float(self.set_lon1.get())
            lat2 = float(self.set_lat2.get())
            lon2 = float(self.set_lon2.get())

            slug = get_map_image(lat1, lon1, lat2, lon2)
            DetailView(parent=self, slug=slug)
            
        except ValueError:
            print("Erro nas coordenadas. Verifique se digitou apenas números.")

    def relatorio(self):
        Relatorio(parent=self)

    def add_marker_event(self,coords,id):
        debug_print(f"coordinate selected {id}: {coords}")
        if id == 1:
            self.set_lat1.delete(0, tk.END)
            self.set_lat1.insert(0, str(coords[0]))
            self.set_lon1.delete(0, tk.END)
            self.set_lon1.insert(0, str(coords[1]))
        else:
            self.set_lat2.delete(0, tk.END)
            self.set_lat2.insert(0, str(coords[0]))
            self.set_lon2.delete(0, tk.END)
            self.set_lon2.insert(0, str(coords[1]))
        
        #Se os 4 campos não estiverem vazios, desenha o retângulo automaticamente (não funciona para colocar as coordenadas manualmente!)
        if self.set_lat1.get() and self.set_lon1.get() and self.set_lat2.get() and self.set_lon2.get():
            self.capturar_entradas_e_desenhar()

    def get_cords(self):
        debug_print("moving map to set coords")
        lat_text = self.set_lat.get()
        lon_text = self.set_long.get()

        try:
            lat = float(lat_text)
            long = float(lon_text)

            self.map_widget.set_position(lat, long)
            self.map_widget.set_zoom(12)
        except ValueError:
            print("Por favor, digite apenas números válidos")

    def desenhar_regiao_geografica(self, lat1, lon1, lat2, lon2):
        debug_print("drawing selection")
        if hasattr(self, 'poligono_selecao') and self.poligono_selecao:
            self.poligono_selecao.delete()

        ponto_superior_esquerdo = (lat1, lon1)
        ponto_superior_direito = (lat1, lon2)
        ponto_inferior_direito = (lat2, lon2)
        ponto_inferior_esquerdo = (lat2, lon1)

        cent_lat = (lat1+lat2)/2
        cent_lon = (lon1+lon2)/2

        if self.selection_marker is not None:
            self.selection_marker.delete()
            self.selection_marker = None

        self.selection_marker = self.map_widget.set_marker(cent_lat, cent_lon, text="centro")

        selection_path = [
            ponto_superior_esquerdo,
            ponto_superior_direito,
            ponto_inferior_direito,
            ponto_inferior_esquerdo
        ]

        self.poligono_selecao = self.map_widget.set_polygon(
            selection_path,
            fill_color=None,
            outline_color="red",
            border_width=3,
            name="regiao_marcada"
        )

    def capturar_entradas_e_desenhar(self):
        debug_print("getting selection data")
        try:
            lat1 = float(self.set_lat1.get())
            lon1 = float(self.set_lon1.get())
            lat2 = float(self.set_lat2.get())
            lon2 = float(self.set_lon2.get())

            self.desenhar_regiao_geografica(lat1, lon1, lat2, lon2)

        except ValueError:
            print("Erro de digitação: Certifique-se de preencher todos os campos apenas com números e usar ponto (ex: -27.59) em vez de vírgula.")

    def limpar_marcacao(self):
        debug_print("delete selection")
        if hasattr(self, 'poligono_selecao') and self.poligono_selecao:
            self.poligono_selecao.delete()
            self.poligono_selecao = None

        if hasattr(self, 'rect_id') and self.rect_id:
            self.map_widget.canvas.delete(self.rect_id)
            self.rect_id = None

        if self.selection_marker is not None:
            self.selection_marker.delete()
            self.selection_marker = None

        self.set_lat1.delete(0, tk.END)
        self.set_lon1.delete(0, tk.END)
        self.set_lat2.delete(0, tk.END)
        self.set_lon2.delete(0, tk.END)

        print("Marcação e coordenadas apagadas com sucesso.")


class Relatorio(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Histórico de Buscas")
        self.geometry("833x558")
        self.configure(bg="#2C3E50")

        self.frames_da_tela()
        self.lista_frame2()

        dados_recebidos = get_all_history()
        self.preencher_lista(dados_recebidos)

    def frames_da_tela(self):
        self.frame_2 = tk.Frame(self, bd=0, bg='#2C3E50')
        self.frame_2.pack(fill="both", expand=True, padx=20, pady=20)

    def lista_frame2(self):
        # Mantemos a declaração original
        self.listaCli = ttk.Treeview(self.frame_2, height=3,
                                     columns=("col1", "col2", "col3", "col4","col5"),
                                     show="headings")

        # Ocultamos a coluna 1 (Slug) zerando a largura e impedindo o redimensionamento
        self.listaCli.column("#1", width=0, stretch=tk.NO)
        self.listaCli.heading("#1", text="")

        # Configuramos as colunas visíveis
        self.listaCli.heading("#2", text="Latitude 1")
        self.listaCli.heading("#3", text="Longitude 1")
        self.listaCli.heading("#4", text="Latitude 2")
        self.listaCli.heading("#5", text="Longitude 2")

        # Centralizamos os textos das colunas visíveis
        self.listaCli.column("#2", width=120, anchor="center")
        self.listaCli.column("#3", width=120, anchor="center")
        self.listaCli.column("#4", width=120, anchor="center")
        self.listaCli.column("#5", width=120, anchor="center")
        
        self.listaCli.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.90)

        self.scroolLista = Scrollbar(self.frame_2, orient="vertical", command=self.listaCli.yview)
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.05, relwidth=0.02, relheight=0.90)

        self.listaCli.bind("<Double-1>", self.click_list)

    def preencher_lista(self, dados):
        for linha_antiga in self.listaCli.get_children():
            self.listaCli.delete(linha_antiga)

        for registro in dados:
            self.listaCli.insert("", "end", values=registro)

    def click_list(self, event):
        selecionado = self.listaCli.selection()
        if not selecionado:
            return
        
        valores_da_linha = self.listaCli.item(selecionado[0], "values")
        DetailView(parent=self, slug=valores_da_linha[0])

       
if __name__ == "__main__":
    app = MainMapWindow()
    app.mainloop()