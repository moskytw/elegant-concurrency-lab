#!/usr/bin/env python


from threading import Thread
from queue import Queue

from operators import op_url_to_text_q, op_text_to_url_q


def start_in_thread(f, *args, **kwargs):
    t = Thread(target=f, args=args, kwargs=kwargs)
    t.start()
    return t


if __name__ == '__main__':

    max_count = 30

    url_q = Queue()
    text_q = Queue()

    url_q.put('https://www.python.org/')

    for _ in range(10):
        start_in_thread(op_url_to_text_q, url_q, text_q, max_count)

    for _ in range(2):
        start_in_thread(op_text_to_url_q, text_q, url_q)
