"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable, Any, List, Iterator

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


def mul(x: float, y: float) -> float:
    return x * y


def id(x: float) -> float:
    return x


def add(x: float, y: float) -> float:
    return x + y


def neg(x: float) -> float:
    return -x


def lt(x: float, y: float) -> float:
    return float(x < y)


def eq(x: float, y: float) -> float:
    return float(x == y)


def max(x: float, y: float) -> float:
    return y if x < y else x


def is_close(x: float, y: float) -> float:
    return float(abs(x - y) < 1e-2)


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x)) if x >= 0 else math.exp(x) / (1.0 + math.exp(x))


def relu(x: float) -> float:
    return 0.0 if x < 0 else x


def log(x: float) -> float:
    return math.log(x)


def exp(x: float) -> float:
    return math.exp(x)


def log_back(x: float, y: float) -> float:
    return y / x


def inv(x: float) -> float:
    return 1 / x


def inv_back(x: float, y: float) -> float:
    return -y / (x * x)


def relu_back(x: float, y: float) -> float:
    return y if x >= 0 else 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.


def map(iterable: Iterable, function: Callable) -> Iterator:
    for x in iterable:
        yield function(x)


def zipWith(
    first_iterable: Iterable, second_iterable: Iterable, function: Callable
) -> Iterator:
    for x, y in zip(first_iterable, second_iterable):
        yield function(x, y)


def reduce(iterable: Iterable, function: Callable, neutral_element: Any = 0):
    result = neutral_element
    for x in iterable:
        result = function(result, x)

    return result


def negList(input: List[float]) -> List[float]:
    return list(map(input, lambda x: -x))


def addLists(first_list: List[float], second_list: List[float]) -> List[float]:
    return list(zipWith(first_list, second_list, lambda x, y: x + y))


def sum(ls: List[float]) -> float:
    return reduce(ls, lambda x, y: x + y)


def prod(ls: List[float]) -> float:
    return reduce(ls, lambda x, y: x * y, 1)
