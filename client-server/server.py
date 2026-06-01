import zmq

def processRequest(message):
    parts = message.split()

    command = parts[0].upper()

    if command == "SOMA":
        return str(float(parts[1]) + float(parts[2]))

    elif command == "SUB":
        return str(float(parts[1]) - float(parts[2]))

    elif command == "MULT":
        return str(float(parts[1]) * float(parts[2]))

    elif command == "DIV":
        if float(parts[2]) == 0:
            return "ERRO: divisao por zero"

        return str(float(parts[1]) / float(parts[2]))

    elif command == "CONCAT":
        return " ".join(parts[1:])

    else:
        return "ERRO: comando desconhecido"


def server():
    context = zmq.Context()

    socket = context.socket(zmq.REP)

    socket.bind("tcp://*:12345")

    print("Servidor aguardando requisicoes...")

    while True:

        message = socket.recv().decode()

        if message == "STOP":
            socket.send(b"Servidor encerrado")
            break

        response = processRequest(message)

        socket.send(response.encode())


if __name__ == "__main__":
    server()