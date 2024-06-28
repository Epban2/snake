from play_game import Game
import tkinter as tk
from tkinter import ttk  # Importiamo ttk per la combobox

class SelectBoxApp:
    def __init__(self, root):
        self.game=Game()

        self.root = root
        self.root.title("Menu")

        # Creiamo una Label per mostrare la selezione
        self.label = tk.Label(root, text="Seleziona un'opzione")
        self.label.pack(pady=10)

        # Creiamo una Combobox (SelectBox)
        self.select_box = ttk.Combobox(root, values=["Riprova", "Esci", "Elimina highscore"])
        self.select_box.set("Scegli un'opzione")  # Imposta il testo predefinito
        self.select_box.pack(pady=10)
        self.select_box.bind("<<ComboboxSelected>>", self.on_select)

    def on_select(self, event):
        # Ottieni il valore selezionato
        scelta = self.select_box.get()

        if scelta=="Riprova":
            self.game.screen.clear()
            self.game.__init__()
            
        elif scelta=="Esci":
            self.root.destroy()
            self.game.screen.bye()
            #blocco mancante
        else:
            with open("scores.txt", "w") as file:
                file.write("0")
            
if __name__ == "__main__":
    root = tk.Tk()
    app = SelectBoxApp(root)
    root.mainloop()

