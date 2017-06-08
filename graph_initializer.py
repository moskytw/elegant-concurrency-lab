#!/usr/bin/env python


from threading import Thread
from queue import Queue

from channel_operators import (
    init_url_q,
    put_text_q,
    put_url_q,
)


def start_in_thread(f, *args, **kwargs):
    t = Thread(target=f, args=args, kwargs=kwargs)
    t.start()
    return t


if __name__ == '__main__':

    run_q = Queue()
    url_q = Queue()
    text_q = Queue()

    init_url_q(url_q)

    for _ in range(8):
        # put_text_q: run_q -> run_q, url_q -> text_q
        start_in_thread(put_text_q, run_q, url_q, text_q)

    for _ in range(4):
        # put_url_q: run_q -> run_q, text_q -> url_q
        start_in_thread(put_url_q, run_q, text_q, url_q)
