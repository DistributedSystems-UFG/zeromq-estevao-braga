import zmq
import pickle
import random
import time

from constPipe import *

def producer():
    context = zmq.Context()

    socket = context.socket(zmq.PUSH)

    socket.bind(f"tcp://*:{PORT_STAGE1}")

    print("Producer iniciado")

    while True:

        task = {
            "id": random.randint(1000, 9999),
            "value": random.randint(1, 100)
        }

        print(f"[PRODUCER] Produzindo {task}")

        socket.send(pickle.dumps(task))

        time.sleep(1)

if __name__ == "__main__":
    producer()