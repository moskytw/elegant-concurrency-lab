#!/usr/bin/env python


import requests
from bs4 import BeautifulSoup


PYCON_TW_ROOT_URL = 'https://tw.pycon.org/'


# conform accessing only its frame


def query_text(url):
    return requests.get(url).text


def parse_out_href_gen(text):
    # soup is bs4.BeautifulSoup
    # a_tag is bs4.element.Tag
    soup = BeautifulSoup(text, 'html.parser')
    return (a_tag.get('href', '') for a_tag in soup.find_all('a'))


def is_relative_href(url):
    return not url.startswith('http') and not url.startswith('mailto:')


# conform using atomic operators


url_visted_map = {}


def is_visited_or_mark(url):

    visited = url_visted_map.get(url, False)
    if not visited:
        url_visted_map[url] = True

    return visited


if __name__ == '__main__':

    # test cases

    print('Testing query_text ... ', end='')
    text = query_text('https://tw.pycon.org')
    print(repr(text[:40]))

    print('Testing parse_out_href_gen ... ', end='')
    href_gen = parse_out_href_gen(text)
    print(repr(list(href_gen)[:3]))

    print('Testing is_relative_href ...')
    assert is_relative_href('2017/en-us')
    assert is_relative_href('/2017/en-us')
    assert not is_relative_href('https://www.facebook.com/pycontw')
    assert not is_relative_href('mailto:organizers@pycon.tw')

    print('Testing is_visited_or_mark ...')
    assert not is_visited_or_mark('/')
    assert is_visited_or_mark('/')

    # benchmark

    from time import time

    print('Benchmarking query_text ... ', end='')  # 40x
    s = time()
    text = query_text('https://tw.pycon.org')
    e = time()
    print(f'{e-s:.4}s')

    print('Benchmarking parse_out_href_gen ... ', end='')  # 1x
    s = time()
    list(parse_out_href_gen(text))
    e = time()
    print(f'{e-s:.4}s')
