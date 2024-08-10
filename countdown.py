from datetime import datetime

# Sample Input:
# Learn Python:10/08/2024
def main():
  user_input = input("Enter the goal with your deadline. Separated by colon. The expected format is DD/MM/YYYY\n")
  goal_with_dealine = user_input.strip().split(":")

  goal = goal_with_dealine[0]
  deadline = goal_with_dealine[-1]
  deadline_date = datetime.strptime(deadline, "%d/%m/%Y")
  date_today = datetime.today()
  time_left = deadline_date - date_today

  if time_left.days <= 0:
    print("No time left")
  else:
    print(f"Time left for: '{goal}' is {time_left.days} days.")

main()
