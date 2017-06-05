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
    print(f'Run with abs      {expt:.4}s  {expt/ctrl:.4}x')

    expt = timeit(run_with_nothing)
    print(f'Run with nothing  {expt:.4}s  {expt/ctrl:.4}x')

    expt = timeit(run_with_lock)
    print(f'Run with lock     {expt:.4}s  {expt/ctrl:.4}x')

    expt = timeit(run_with_rlock)
    print(f'Run with rlock    {expt:.4}s  {expt/ctrl:.4}x')
