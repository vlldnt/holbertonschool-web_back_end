#!/usr/bin/env python3
"""Module for executing multiple tasks"""


from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int=10) -> List[float]:
    '''Spawns wait_random n times and returns list of delays in ascending'''
    delays = [wait_random(max_delay) for _ in range(n)]
    delay = await asyncio.gather(*delays)
    return sorted(delay)
