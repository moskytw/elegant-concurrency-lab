#!/usr/bin/env python
# -*- coding: utf-8 -*-


from timeit import timeit
from threading import Lock, RLock


x = 0
lock = Lock()
rlock = RLock()


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


if __name__ == '__main__':

    ctrl = expt = timeit(run_with_abs)
    print(f'Run with abs      {expt:<06.4}s  {expt/ctrl:<06.4}x')

    expt = timeit(run_with_nothing)
    print(f'Run with nothing  {expt:<06.4}s  {expt/ctrl:<06.4}x')

    expt = timeit(run_with_lock)
    print(f'Run with lock     {expt:<06.4}s  {expt/ctrl:<06.4}x')

    expt = timeit(run_with_rlock)
    print(f'Run with rlock    {expt:<06.4}s  {expt/ctrl:<06.4}x')

    # Run with abs      0.4113s  1.0000x
    # Run with nothing  0.2348s  0.5709x
    # Run with lock     0.6629s  1.6110x
    # Run with rlock    0.6630s  1.6120x
