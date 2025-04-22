#!/usr/bin/env python3
"""Module for concurrent coroutines"""


import random
from time import sleep

async def wait_random(max_delay: int = 10) -> float:
    wait = random.uniform(0, max_delay)
    sleep(wait)
    return wait
