#!/usr/bin/env python


from collections import deque

from atoms import query_text, parse_to_url_gen, keep_external_url_gen, inc_count


if __name__ == '__main__':

    max_count = 10

    q = deque()
    q.append('https://www.python.org/')

    while True:

        if inc_count() > max_count:
            print('Reach max_count', max_count, '...')
            break

        url = q.popleft()
        print('Querying', url, '...')
        text = query_text(url)

        print('Parsing ...')
        q.extend(keep_external_url_gen(parse_to_url_gen(text)))
