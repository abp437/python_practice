# Import statement for built in packages
import re
from utils.validate_numbers import validate_number as validate_number_input

def calculate_hours(days):
  day_count = validate_number_input(days)

  if day_count <= 0:
    print("Number of days is invalid")
    return 0

  return day_count * 24

# Expected Input Format: [12, 34, 56, 834, 34, 455, 'asdds', 34.34]
def list_main():
  user_input = input("Enter a comma separated array. It must be enclosed within '[]':\n")
  list_brackets_removal = user_input[1:-1]
  white_spaces_removal = re.sub(r'\s+', '', list_brackets_removal)
  list_of_numbers = white_spaces_removal.split(',')

  for number in list_of_numbers:
    print(f"For {number} days, the number of hours are {calculate_hours(number)}\n")

list_main()
