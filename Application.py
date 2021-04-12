import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Text-based Game')

        title = tk.Label(self, text='A text-based Game', font=10)
        title.pack(pady=2, padx=2)

        start_button = tk.Button(self, text='Click to start!', command=start_game)
        start_button.pack(pady=5, padx=5)

        name_entry = tk.Entry(self, width=30)
        name_entry.pack(padx=7, pady=7)

def start_game():
    input = input("Press any key to start the game...")
    answer = input("You reach a crossroad, would you like")
