#!/usr/bin/env python3
"""Module for concurrent coroutines"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''Sleep for few sec (float)'''
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
