#!/usr/bin/env python
"""Make a password"""

import string
import random
import sys

CHARACTERS = list(string.letters + string.digits + '!@#$&%^')


def make_password(lenght=8):
  """Make a password."""
  assert lenght >= 4

  characters = CHARACTERS * (lenght / len(CHARACTERS) + 1)
  random.shuffle(characters)

  while True:
    password = ''.join(random.sample(characters, lenght))
    if all([any(c in string.lowercase for c in password),
            any(c in string.uppercase for c in password),
            any(c in string.digits for c in password),
            any(c in string.punctuation for c in password)]):
      return password


def main(args):
  """Hooray for main."""
  if not args:
    args.append(8)
  length = int(args[0])
  print make_password(length)


if __name__ == '__main__':
  main(sys.argv[1:])
