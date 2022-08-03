from typing import Dict
from asyncio import Queue, QueueEmpty as Empty


QUEUE = {}

def add_to_queue(chat_id, title, duration, ytlink, playlink, type, quality, thumb):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.append([title, duration, ytlink, playlink, type, quality, thumb])
        return int(len(chat_queue) - 1)
    else:
        QUEUE[chat_id] = [[title, duration, ytlink, playlink, type, quality, thumb]]


def get_queue(chat_id):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        return chat_queue
    else:
        return 0


def pop_an_item(chat_id):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.pop(0)
        return 1
    else:
        return 0


def clear_queue(chat_id):
    if chat_id in QUEUE:
        QUEUE.pop(chat_id)
        return 1
    else:
        return 0


async def put(chat_id: int, **kwargs) -> int:
    if chat_id not in queues:
        queues[chat_id] = Queue()
    await queues[chat_id].put({**kwargs})
    return queues[chat_id].qsize()



def is_empty(chat_id: int) -> bool:
    if chat_id in queues:
        return queues[chat_id].empty()
    return True


def task_done(chat_id: int):
    if chat_id in queues:
        try:
            queues[chat_id].task_done()
        except ValueError:
            pass
