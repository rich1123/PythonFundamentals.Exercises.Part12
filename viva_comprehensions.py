from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start: int at the beginning of the range (inclusive)
    :param stop: int at the beginning of the range (exclusive)
    :param parity:
    :return:
    """

    # parity = lambda: x % 2 != 0
    return [x for x in range(start, stop) if x % 2 != parity.value]


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """

    return {x: strategy(x) for x in range(start, stop)}


def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """

    return {c.upper() for c in val_in if c == c.lower()}

