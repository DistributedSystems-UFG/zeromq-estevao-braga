import zmq

SERVER_IP = "IP_DO_SERVIDOR"

def client():

    context = zmq.Context()

    socket = context.socket(zmq.REQ)

    socket.connect(f"tcp://{SERVER_IP}:12345")

    commands = [
        "SOMA 10 20",
        "SUB 30 12",
        "MULT 7 8",
        "DIV 100 5",
        "CONCAT Sistemas Distribuidos com ZeroMQ"
    ]

    for cmd in commands:

        print(f"Enviando: {cmd}")

        socket.send(cmd.encode())

        reply = socket.recv().decode()

        print(f"Resposta: {reply}\n")

    socket.send(b"STOP")

    print(socket.recv().decode())


if __name__ == "__main__":
    client()