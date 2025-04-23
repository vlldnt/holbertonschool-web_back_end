#!/usr/bin/env python3
"""
function asynchronus wait a random delay and returns it in float value
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Method: wait_random - wait a rndm amount of time
    Parameter: max_delay - a delay of up to 10 seconds
    Return: the ammount of time of the delay
    """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
