from tkinter import *

class Menu_lateral(Frame):
    def __init__(self, parent, comando_ir_mapa, comando_ir_inicio, comando_ir_dados, comando_ir_relatorios):

        super().__init__(parent, bg="#108cff", width=200,height=500)

        self.pack(side="left", fill="y")

        self.pack_propagate(False)

        self.sidebar_expand = True
        self.toggle_button = Button(self, text="menu", bg="#034787", fg="white", cursor="hand2",  font=("Arial", 16), relief = "flat", command=self.toggle_sidebar)

        self.toggle_button.pack(pady=10, padx=10, fill="x", anchor="w")
        self.nav_buttons = []
        
        #---------------------------------------------

        btn_mapa = Button(self, text="Mapa", bg="#034787", fg="white", font=("Arial",14), relief="flat", cursor="hand2", anchor="w", command=comando_ir_mapa)
        btn_mapa.pack(fill="x", pady=5, padx=10)
        self.nav_buttons.append(btn_mapa)

        #---------------------------------------------

        btn_dados = Button(self, text="Dados", bg="#034787", fg="white", font=("Arial", 14), relief="flat", cursor="hand2", anchor="w", command=comando_ir_dados)
        self.nav_buttons.append(btn_dados)

        #---------------------------------------------

        btn_relatorio = Button(self, text="Relatorios", bg="#034787", fg="white", font=("Arial", 14), relief="flat", cursor="hand2", anchor="w", command=comando_ir_relatorios)
        self.nav_buttons.append(btn_relatorio)

        #---------------------------------------------

        btn_equipe = Button(self, text="Equipe", bg="#034787", fg="white", font=("Arial", 14), relief="flat", cursor="hand2", anchor="w", command=comando_ir_inicio)
        self.nav_buttons.append(btn_equipe)

        #---------------------------------------------

        btn_close = Button(self, text="Close", bg="#034787", fg="red", font=("Arial",14), relief="flat", cursor="hand2", anchor="w", command=self.master.destroy)
        btn_close.pack(fill="x", pady=5, padx=10)
        self.nav_buttons.append(btn_close)
        self.toggle_sidebar()

    def toggle_sidebar(self):

        if self.sidebar_expand:
            self.config(width=50)
            self.toggle_button.config(text="☰", font=("Arial",12))
            for btn in self.nav_buttons:
                btn.pack_forget()
            self.sidebar_expand = False
           
        else:
            self.config(width=200)
            self.toggle_button.config(text="☰", font=("Arial", 16))
            for btn in self.nav_buttons:
                btn.pack(fill="x", pady=5, padx=10)
            self.sidebar_expand = True
            
       