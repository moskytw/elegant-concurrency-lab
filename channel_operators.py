#!/usr/bin/env python


import logging
from urllib.parse import urljoin

from atomic_utils import (
    PYCON_TW_ROOT_URL,
    query_text,
    parse_out_href_gen,
    is_relative_href,
    is_visited_or_mark,
)


# https://docs.python.org/3.6/library/logging.html#logrecord-attributes
logging.basicConfig(
    format=(
        '%(asctime)s\t'
        #'%(name)s\t'
        '%(levelname)s\t'
        #'%(processName)s\t'
        '%(threadName)s\t'
        #'%(module)s:'
        '%(funcName)s:%(lineno)d\t'
        '%(message)s'
    ),
    level=logging.DEBUG
)
l = logging.getLogger('channel_operators')


# make a distinguishing and debuggable object
TO_RETURN = ['to_return']


def init_url_q(url_q):
    url_q.put(PYCON_TW_ROOT_URL)


def put_text_q(url_q, text_q):

    while True:

        l.info(f'url_q: {url_q.qsize()}')
        url = url_q.get()
        l.info(f'url_q.get() -> {url}')

        if url is TO_RETURN:
            url_q.put(TO_RETURN)  # broadcast to siblings
            return

        text = query_text(url)
        text_q.put(text)


def put_url_q(text_q, url_q):

    while True:

        l.info(f'text_q: {text_q.qsize()}')
        text = text_q.get()
        l.info(f'len(text_q.get()) -> {len(text)}')

        if text is TO_RETURN:
            text_q.put(TO_RETURN)
            return

        href_gen = parse_out_href_gen(text)

        put_count = 0
        for href in href_gen:

            if not is_relative_href(href):
                continue

            url = urljoin(PYCON_TW_ROOT_URL, href)
            if is_visited_or_mark(url):
                continue

            url_q.put(url)
            put_count += 1

        l.info(f'Determining to cut the loop ...')
        l.info(f'url_q: {url_q.qsize()}')
        l.info(f'text_q: {text_q.qsize()}')
        l.info(f'put_count: {put_count}')
        if url_q.qsize() == 0 and text_q.qsize() == 0 and put_count == 0:
            text_q.put(TO_RETURN)
            url_q.put(TO_RETURN)
            return
