from .guitar import Guitar

class ElectricGuitar(Guitar):
  def __init__(self, strings_count=8) -> None:
    # `super()` constructor is called here.
    super().__init__(strings_count)

  def play_louder(self):
    print(super().get_tone().upper())
