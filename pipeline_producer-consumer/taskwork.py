import zmq
import pickle

from constPipe import *

context = zmq.Context()

receiver = context.socket(zmq.PULL)

receiver.connect(
    f"tcp://{PRODUCER_IP}:{PORT_STAGE1}"
)

sender = context.socket(zmq.PUSH)

sender.bind(
    f"tcp://*:{PORT_STAGE2}"
)

print("Worker1 iniciado")

while True:

    task = pickle.loads(receiver.recv())

    print(f"[WORKER1] Recebido {task}")

    task["square"] = task["value"] ** 2

    print(f"[WORKER1] Processado {task}")

    sender.send(pickle.dumps(task))