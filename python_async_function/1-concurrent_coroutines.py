#!/usr/bin/env python3
"""Module for concurrent coroutines"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Spawns wait_random n times and returns list of delays in ascending'''
    delays = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(delays)]
