import multiprocessing
import zmq
import pickle
import random
import time
import math

PORT1 = 5555
PORT2 = 5556

def producer():

    context = zmq.Context()

    socket = context.socket(zmq.PUSH)

    socket.bind(f"tcp://*:{PORT1}")

    while True:

        task = {
            "id": random.randint(1000, 9999),
            "value": random.randint(1, 100)
        }

        print(f"[PRODUCER] {task}")

        socket.send(pickle.dumps(task))

        time.sleep(1)

def worker1():

    context = zmq.Context()

    receiver = context.socket(zmq.PULL)

    receiver.connect(
        f"tcp://localhost:{PORT1}"
    )

    sender = context.socket(zmq.PUSH)

    sender.bind(
        f"tcp://*:{PORT2}"
    )

    while True:

        task = pickle.loads(receiver.recv())

        task["square"] = task["value"] ** 2

        print(f"[WORKER1] {task}")

        sender.send(pickle.dumps(task))

def worker2():

    context = zmq.Context()

    receiver = context.socket(zmq.PULL)

    receiver.connect(
        f"tcp://localhost:{PORT2}"
    )

    while True:

        task = pickle.loads(receiver.recv())

        task["sqrt"] = round(
            math.sqrt(task["square"]),
            2
        )

        print(f"[WORKER2] {task}")

if __name__ == "__main__":

    p1 = multiprocessing.Process(
        target=producer
    )

    p2 = multiprocessing.Process(
        target=worker1
    )

    p3 = multiprocessing.Process(
        target=worker2
    )

    p1.start()
    p2.start()
    p3.start()

    time.sleep(60)

    p1.terminate()
    p2.terminate()
    p3.terminate()