#!/usr/bin/env python
# -*- coding: utf-8 -*-


from threading import Thread
from queue import Queue

import requests


# make a distinguishing and debuggable object
TO_RETURN = ['to_return']


def consume_url_q(url_q):

    while True:

        url = url_q.get()

        if url is TO_RETURN:
            return

        content = requests.get(url).content
        print('Queried', len(content), 'bytes from', url)


def call_in_thread(f, *args, **kwargs):
    t = Thread(target=f, args=args, kwargs=kwargs)
    t.start()
    return t


if __name__ == '__main__':

    N = 2

    urls = [
        'https://tw.pycon.org/',
        'https://tw.pycon.org/2017/en-us/events/keynotes/',
        'https://tw.pycon.org/2017/en-us/events/schedule/',
        'https://tw.pycon.org/2017/en-us/venue/',
    ]

    url_q = Queue()
    for url in urls:
        url_q.put(url)

    for _ in range(N):
        url_q.put(TO_RETURN)

    for _ in range(N):
        call_in_thread(consume_url_q, url_q)
