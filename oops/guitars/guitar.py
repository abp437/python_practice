class Guitar:
  # Default arguments used here.
  def __init__(self, strings_count=6) -> None:
    self.strings_count = strings_count
    self.tone = "Om Om Om Om"

  def get_tone(self):
    return self.tone

  def play(self):
    print(self.get_tone())
