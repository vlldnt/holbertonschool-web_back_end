#!/usr/bin/env python3
"""Module for concurrent coroutines"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''Asynchronus function corroutine'''
    delay: float = [wait_random(max_delay) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delay)]
