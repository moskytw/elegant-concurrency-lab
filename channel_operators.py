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


# make distinguishing and debuggable objects
RUNNING = ['running']
TO_RETURN = ['to_return']


def init_url_q(url_q):
    is_visited_or_mark(PYCON_TW_ROOT_URL)
    url_q.put(PYCON_TW_ROOT_URL)


def put_text_q(url_q, text_q, run_q):

    while True:

        # the below get and put should be synced
        # but for the readability, keep as it is

        l.info(f'url_q: {url_q.qsize()}')
        url = url_q.get()
        l.info(f'url_q.get() -> {url}')

        run_q.put(RUNNING)
        l.info('run_q.put(RUNNING)')

        if url is TO_RETURN:
            url_q.put(TO_RETURN)  # broadcast to siblings
            l.info('return')
            return

        text = query_text(url)
        text_q.put(text)

        run_q.get()
        l.info('run_q.get()')


def put_url_q(text_q, url_q, run_q):

    while True:

        l.info(f'text_q: {text_q.qsize()}')
        text = text_q.get()
        l.info(f'len(text_q.get()) -> {len(text)}')

        run_q.put(RUNNING)
        l.info('run_q.put(RUNNING)')

        if text is TO_RETURN:
            text_q.put(TO_RETURN)
            l.info('return')
            return

        href_gen = parse_out_href_gen(text)

        for href in href_gen:

            if not is_relative_href(href):
                continue

            url = urljoin(PYCON_TW_ROOT_URL, href)
            if is_visited_or_mark(url):
                continue

            url_q.put(url)

        l.info(f'url_q: {url_q.qsize()}')
        l.info(f'run_q: {run_q.qsize()}')
        if url_q.qsize() == 0 and run_q.qsize() == 1:
            url_q.put(TO_RETURN)
            text_q.put(TO_RETURN)
            l.info('url_q.put(TO_RETURN)')
            l.info('text_q.put(TO_RETURN)')

        run_q.get()
        l.info('run_q.get()')
