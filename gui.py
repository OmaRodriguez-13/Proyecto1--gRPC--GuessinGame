import grpc
import guess_pb2
import guess_pb2_grpc
from tkinter import *
from tkinter import messagebox, simpledialog
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font

class GuessClient:
    def __init__(self, stub):
        self.stub = stub
        self.window = Tk()
        self.window.title("Juego de adivinar el número")
        self.window.geometry("300x150")
        self.window.resizable(False, False)
        self.label = Label(self.window, text="Adivina un número entre 1 y 100:")
        self.label.pack(pady=10)
        self.entry = Entry(self.window, width=10)
        self.entry.pack()
        self.button = Button(self.window, text="Adivinar", command=self.guess_number)
        self.button.pack(pady=10)

         # Centrar ventana en la pantalla
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.window.mainloop()

    
    def guess_number(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número entero.")
            return

        if guess < 1 or guess > 100:
            messagebox.showerror("Error", "Por favor ingrese un número entre 1 y 100.")
            return

        response = self.stub.guessNumber(guess_pb2.GuessRequest(guess=guess))
        messagebox.showinfo("Respuesta", response.message)

def run():
    ip = simpledialog.askstring("Dirección IP del servidor", "Ingrese la  IP del servidor.")
    server_address = ip + ":50051"
    channel = grpc.insecure_channel(server_address) 
    stub = guess_pb2_grpc.GuessServiceStub(channel)
    GuessClient(stub)

if __name__ == '__main__':
    run()
