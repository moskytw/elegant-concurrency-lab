#!/usr/bin/env python


from threading import Thread
from queue import Queue

from channel_operators import (
    init_url_q,
    put_text_q,
    put_url_q,
)


def call_in_thread(f, *args, **kwargs):
    t = Thread(target=f, args=args, kwargs=kwargs)
    t.start()
    return t


if __name__ == '__main__':

    import sys

    args = (8, 4)
    if len(sys.argv) == 3:
        args = (int(sys.argv[1]), int(sys.argv[2]))

    url_q = Queue()
    text_q = Queue()
    run_q = Queue()

    init_url_q(url_q)

    for _ in range(args[0]):
        # put_text_q:
        #   url_q -> text_q
        #   run_q
        call_in_thread(put_text_q, url_q, text_q, run_q)

    for _ in range(args[1]):
        # put_url_q:
        #   text_q -> url_q
        #   run_q
        call_in_thread(put_url_q, text_q, url_q, run_q)
