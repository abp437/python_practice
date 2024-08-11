# Relative import used rather than a Package type import
from .guitar import Guitar

# Just the same implementation and functionality as the parent class.
class ClassicGuitar(Guitar):
  def __init__(self) -> None:
    super().__init__()  # Initialize the parent class
