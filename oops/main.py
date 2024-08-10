from user import User

try:
  user = User(
    name = "Stone Cold",
    email = "austin@wwf.com",
    age = -29,
    password = "austin gives the stunner",
    permanent_job_title = "Toughest SOB"
  )
except ValueError as e:
  print(e)

user = User(
  name = "Akshay Pawar",
  email = "abp437@gmail.com",
  age = 29,
  password = "austin gives the stunner",
  permanent_job_title = "Founder & CEO"
)

user.get_user_info()
