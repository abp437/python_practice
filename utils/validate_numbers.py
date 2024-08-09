import math

def validate_number(input):
  if isinstance(input, int): return input
  if input.isdigit(): return int(input)

  res = 0

  try:
    parsed = float(input)
    res = math.floor(parsed)
  except ValueError:
    res = 0

  return res
