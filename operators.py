#!/usr/bin/env python


from atoms import get_text, parse_to_url_gen, keep_external_url_gen, inc_count


TO_RETURN = None


def op_url_to_text_q(url_q, text_q, max_count):

    while True:

        if inc_count() > max_count:
            text_q.put(TO_RETURN)
            return

        url = url_q.get()
        print('Visiting', url, '...')
        text = get_text(url)
        text_q.put(text)


def op_text_to_url_q(text_q, url_q):

    while True:

        text = text_q.get()
        if text is TO_RETURN:
            text_q.put(TO_RETURN)
            return

        print('Parsing ...')
        for url in keep_external_url_gen(parse_to_url_gen(text)):
            url_q.put(url)
