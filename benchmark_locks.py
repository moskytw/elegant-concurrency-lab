#!/usr/bin/env python
# -*- coding: utf-8 -*-


from timeit import timeit
from threading import Lock, RLock
from queue import Queue


x = 0
lock = Lock()
rlock = RLock()
queue = Queue()
queue.put(1)  # = the get won't block = released lock


def run_with_nothing():
    x+1


def run_with_abs():
    abs(1)
    x+1
    abs(1)


def run_with_lock():
    lock.acquire()
    x+1
    lock.release()


def run_with_rlock():
    rlock.acquire()
    x+1
    rlock.release()


def run_with_queue():
    queue.get()  # let other gets block
    x+1
    queue.put(1)  # let one get continue


if __name__ == '__main__':

    N = 1000000  # the default value

    ctrl = expt = timeit(run_with_abs, number=N)
    print(f'Run with abs      {expt:6.4f}s  {expt/ctrl:7.4f}x')

    expt = timeit(run_with_nothing, number=N)
    print(f'Run with nothing  {expt:6.4f}s  {expt/ctrl:7.4f}x')

    expt = timeit(run_with_lock, number=N)
    print(f'Run with lock     {expt:6.4f}s  {expt/ctrl:7.4f}x')

    expt = timeit(run_with_rlock, number=N)
    print(f'Run with rlock    {expt:6.4f}s  {expt/ctrl:7.4f}x')

    expt = timeit(run_with_queue, number=N//10)*10
    print(f'Run with queue    {expt:6.4f}s  {expt/ctrl:7.4f}x')

    # Run with abs      0.3458s   1.0000x
    # Run with nothing  0.1982s   0.5732x
    # Run with lock     0.6050s   1.7495x
    # Run with rlock    0.6192s   1.7907x
    # Run with queue    7.4945s  21.6723x
