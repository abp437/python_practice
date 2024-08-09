import math

# In python we have to define the function before it's called.
# There's no concept of hoisting in it, even if it's an interpreted language.
def validate_number_input(input):
  if isinstance(input, int): return input
  if input.isdigit(): return int(input)

  res = 0

  try:
    parsed = float(input)
    res = math.floor(parsed)
  except ValueError:
    res = 0

  return res

def calculate_hours(days):
  day_count = validate_number_input(days)

  if day_count <= 0:
    print("Number of days is invalid")
    return 0

  return day_count * 24

def main():
  user_input = input("Hello, please enter the number of days and I'll calculate the number of hours in it. \n")
  print(f"The number of hours are {calculate_hours(user_input)}")

main()
