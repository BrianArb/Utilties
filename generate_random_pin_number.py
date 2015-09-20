#!/usr/bin/env python
"""Make a random pin number.

Usage: generate_random_pin_number.py [interger]
"""

from __future__ import print_function

import string
import random
import sys

DEFAULT = 4
CHARACTERS = list(string.digits)


def print_usage(error_message):
  """Print user friendly error message and exit.

  Args:
    error_message: str, the error message to print.
  """
  print(error_message, file=sys.stderr)
  print()
  print(__doc__, file=sys.stderr)
  sys.exit(1)


def make_pin_number(lenght=DEFAULT):
  """Make a random pin number.

  Args:
    lenght: digit 1 or greater, the lenght of the pin to make.
  Return:
    str, the random pin number generated.
  """
  try:
    lenght = int(lenght)
    assert lenght >= 1
  except ValueError:
    error_msg = 'Expected a interger got "{0}" instead.'
    print_usage(error_msg.format(lenght))
  except AssertionError:
    error_msg = 'Expected a interger greater or equal to 1. got {0} instead.'
    print_usage(error_msg.format(lenght))

  characters = CHARACTERS * (lenght / len(CHARACTERS) + 1)
  random.shuffle(characters)
  return ''.join(random.sample(characters, lenght))


def main(args):
  """Hooray for main."""
  length = args[0] if args else DEFAULT
  print(make_pin_number(length))


def tests():
  assert isinstance(DEFAULT, int)
  assert make_pin_number(DEFAULT).isdigit()
  assert make_pin_number().isdigit()
  assert len(make_pin_number()) == DEFAULT


if __name__ == '__main__':
  tests()
  main(sys.argv[1:2])
