"""
rut.py

This module provides functions for handling Chilean RUTs (Rol Único Tributario).
It includes functions to clean, validate, get the check digit, format, and generate RUTs.

Authors:
- Valentin Marquez

License:
MIT License

Functions:
- clean(rut: str) -> str
- validate(rut: str) -> bool
- get_check_digit(input: str) -> str
- format(rut: str, dots: bool = True, dash: bool = True) -> str
- generate(n: int = 1) -> str or List[str]
"""
import random
import re
from typing import List, Union


def clean(rut: str) -> str:
    """Function to clean a rut string. Removes all non numeric characters

    Args:
        rut (str): The rut to clean

    Returns:
        str: The cleaned rut
    
    Examples:
        >>> clean("35.114.652-4")
        '351146524'
    """
    return re.sub(r'^0+|[^0-9kK]+', '', rut)


def validate(rut: str) -> bool:
    """Function to validate a rut

    Args:
        rut (str): The rut to validate

    Returns:
        bool: Whether the rut is valid or not

    Examples:
        >>> validate("4612837-0")
        True
    """
    if not isinstance(rut, str):
        return False

    if rut.startswith('0'):
        return False

    if not re.match(r'^0*(\d{1,3}(\.?\d{3})*)-?([\dkK])$', rut):
        return False

    rut = clean(rut)
    t = int(rut[:-1].replace(".", ""))
    m = 0
    s = 1

    while t > 0:
        s = (s + (t % 10) * (9 - (m % 6))) % 11
        t = t // 10
        m += 1

    v = str(s - 1) if s > 0 else 'K'
    return v == rut[-1]


def get_check_digit(digit: str) -> str:
    """Function to get the check digit of a rut

    Args:
        digit (str): The rut to get the check digit from

    Raises:
        ValueError: If the rut is invalid

    Returns:
        str: The check digit

    Examples:
        >>> get_check_digit("60487586")
        '2'
    """
    rut = list(map(int, clean(digit)))

    if len(rut) == 0 or any(map(lambda x: x != x, rut)):
        raise ValueError(f'"{digit}" as RUT is invalid')

    modulus = 11
    sum_result = sum(
        current_value * ((index % 6) + 2)
        for index, current_value in enumerate(reversed(rut))
    )

    check_digit = modulus - (sum_result % modulus)

    if check_digit == 10:
        return 'K'
    elif check_digit == 11:
        return '0'
    else:
        return str(check_digit)


def format_rut(rut: str, dots: bool = True, dash: bool = True) -> str:
    """Function to format a rut

    Args:
        rut (str): The rut to format
        dots (bool, optional): Whether to add dots or not. Defaults to True.
        dash (bool, optional): Whether to add a dash or not. Defaults to True.

    Returns:
        str: The formatted rut

    Examples:
        >>> format_rut("351146524")
        '35.114.652-4'

    """
    rut = clean(rut)
    result = ''

    if dots:
        result = rut[-4:-1] + '-' + rut[-1]
        for i in range(4, len(rut), 3):
            result = rut[-3-i:-i] + '.' + result
    else:
        result = rut[:-1] + '-' + rut[-1]

    if not dash:
        result = result.replace('-', '')

    return result


def generate(num: int = 1) -> Union[str, List[str]]:
    """Generates random valid Chilean RUTs.

    Args:
        num (int, optional): Number of RUTs to generate. Defaults to 1.

    Returns:
        str or List[str]: The generated RUT. If the number is greater than 1, a list of RUTs is returned.
    """
    ruts = []
    for _ in range(num):
        rut_base = random.randint(1000000, 25000000)
        rut = str(rut_base)
        dv = get_check_digit(rut)
        rut = format_rut(rut + dv)
        ruts.append(rut)

    if num == 1:
        return [ruts[0]]

    return ruts
