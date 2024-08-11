class User:
  # Constructor function
  def __init__(self, **kwargs) -> None:
    # `or "Austin"` acts like a default value if the keyword argument isn't provided.
    self.name = kwargs.get('name') or "Austin"
    self.age = kwargs.get('age')

    # Public setter access, no decorators specified, thus no validations applied.
    self.email = kwargs.get('email')
    self.password = kwargs.get('password')
    self.permanent_job_title = kwargs.get('permanent_job_title')

  def get_user_info(self):
    print(f"{self.name} works as {self.permanent_job_title}. He is {self.age} years old. You can contact him at {self.email}.")

  # Private Properties i.e. must have property decorators around it.
  # These private properties must begin with an underscore - `self._name`.
  # To indicate that these must be accessed via decorators and must go through the validations in the setter function.

  @property # Getter
  def name(self):
    return self._name

  @name.setter # Setter
  def name(self, value):
    self._name = value

  @property # Getter
  def age(self):
    return self._age

  @age.setter # Setter with validation
  def age(self, value):
    if value < 0:
      raise ValueError(f"Age cannot be negative for {self._name}.")
    self._age = value
