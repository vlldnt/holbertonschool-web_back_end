#!/usr/bin/env python3
"""Module for measuring runtime"""



wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    