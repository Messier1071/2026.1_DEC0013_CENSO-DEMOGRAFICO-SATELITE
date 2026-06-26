import tkinter as tk
import tkintermapview
from menu_lateral import Menu_lateral
from paginas import Telas


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Mapa")

    tela = Telas(root)
    
    root.mainloop() 