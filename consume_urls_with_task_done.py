#!/usr/bin/env python
# -*- coding: utf-8 -*-


from threading import Thread
from queue import Queue

import requests


def consume_url_q(url_q):

    while True:

        url = url_q.get()

        content = requests.get(url).content
        print('Queried', len(content), 'bytes from', url)

        # mark a task is done
        url_q.task_done()


def call_in_daemon_thread(f, *args, **kwargs):
    t = Thread(target=f, daemon=True, args=args, kwargs=kwargs)
    t.start()
    return t


if __name__ == '__main__':

    urls = [
        'https://tw.pycon.org/',
        'https://tw.pycon.org/2017/en-us/events/keynotes/',
        'https://tw.pycon.org/2017/en-us/events/schedule/',
        'https://tw.pycon.org/2017/en-us/venue/',
    ]

    url_q = Queue()
    for url in urls:
        url_q.put(url)

    for _ in range(2):
        # the “daemon” is not the Unix's deamon
        # daemon threads are abruptly stopped at shutdown
        call_in_daemon_thread(consume_url_q, url_q)

    # block and unblock when all tasks are done
    url_q.join()

    # when main thread exits, the interpreter shuts down
