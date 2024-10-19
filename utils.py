from itertools import tee
import sys

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def input_stations(nodes: list[str]) -> tuple[str, str]:
    print(f'Stations: {nodes}')
    a, b, *_ = sys.argv[1:3] + [None, None]
    while a is None or a not in nodes:
        a = input('Enter first station: ')
    while b is None or b not in nodes:
        b = input('Enter second station: ')
    return a, b

