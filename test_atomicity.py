#!/usr/bin/env python


''' Test the atomicity.

See
https://docs.python.org/3/faq/library.html#what-kinds-of-global-value-mutation-are-thread-safe
for the details.

'''


import sys
from concurrent.futures import ThreadPoolExecutor


sys.setswitchinterval(10**-6)


int_ = 0
list_ = []


def inc():
    global int_
    global list_
    int_ += 1
    list_.append(1)


if __name__ == '__main__':

    with ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(10**3):
            executor.submit(inc)

    print(int_)  # non-atomic
    print(len(list_))  # atomic
