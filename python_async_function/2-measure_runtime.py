#!/usr/bin/env python3
"""Module for measuring runtime"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Def description'''
    start_time = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    return float(elapsed_time / n)

