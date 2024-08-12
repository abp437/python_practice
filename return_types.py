from typing import Union

# `DivisionError` class inherits from `Exception`
class DivisionError(Exception):
  # Below is another way to provide a comment
  """Custom exception for division errors."""
  # Here we've implemented `pass` because we just simply want to inherit from `Exception` and do nothing else.
  pass

# Here we're declaring that the function might either return a `Boolean` or a `DivisionError`. Thus we have to use Union for it.
# We are also declaring the argument types to be of `int` type.
def safe_divide(a: int, b: int) -> Union[bool, DivisionError]:
  """Divide two integers, returning a boolean result or raising an error."""
  if b == 0:
    raise DivisionError("Division by zero")
  return a % b == 0
