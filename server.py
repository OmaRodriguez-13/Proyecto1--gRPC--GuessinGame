from concurrent import futures
import grpc
import guess_pb2
import guess_pb2_grpc
import random
import socket
from tkinter import messagebox

class GuessService(guess_pb2_grpc.GuessServiceServicer):

    def __init__(self, number_to_guess):
        self.number_to_guess = number_to_guess

    def guessNumber(self, request, context):
        if request.guess < self.number_to_guess:
            return guess_pb2.GuessResponse(message="El número es mayor")
        elif request.guess > self.number_to_guess:
            return guess_pb2.GuessResponse(message="El número es menor")
        else:
            return guess_pb2.GuessResponse(message="¡Adivinaste el número!")
            # Obtener la dirección IP del cliente
            ip_address = context.peer().split(':')[0] 
            ip_address = socket.gethostbyname(ip_address)

            print(f"El cliente con dirección IP {context.peer().split(':')[0]} adivinó el número.")
            return guess_pb2.GuessResponse(message="¡Adivinaste el número!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    random_number = random.randint(1, 100) # Generar un número aleatorio entre 1 y 100
    messagebox.showinfo("Random",f"El número aleatorio generado es: {random_number}")
    print(f"El número aleatorio generado es: {random_number}")
    guess_pb2_grpc.add_GuessServiceServicer_to_server(GuessService(random_number), server)
    server.add_insecure_port('[::]:50051')
    messagebox.showinfo("Port", "El servidor está escuchando en el puerto 50051.")
    print("El servidor está escuchando en el puerto 50051.")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
