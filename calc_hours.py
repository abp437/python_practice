import math

# Constants
CMD_STR = ">>> "
DEFAULT_PROMPT = f"Hello, please enter the number of days and I'll calculate the number of hours in it. \nType 'exit' or 'quit' to exit the program. \n{CMD_STR}"

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

# One line functions
def is_exit_string(s): return s == "exit" or s == "quit"

def is_blank(s): return s == ""

def get_prompt_str(iteration, prev_input):
  if iteration == 0: return DEFAULT_PROMPT
  return CMD_STR if is_blank(prev_input) else DEFAULT_PROMPT

def main():
  prev_input = ""
  i = 0

  while True:
    user_input = input(get_prompt_str(i, prev_input))
    prev_input = user_input
    i += 1

    if is_blank(user_input): continue
    if is_exit_string(user_input): return

    print(f"The number of hours are {calculate_hours(user_input)}\n")

main()
