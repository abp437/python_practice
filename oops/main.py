from user import User
from guitars.classic_guitar import ClassicGuitar
from guitars.electric_guitar import ElectricGuitar

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
  age = 30,
  password = "austin gives the stunner",
  permanent_job_title = "Founder & CEO"
)

user.get_user_info()

classic_guitar = ClassicGuitar()
classic_guitar.play()

electric_guitar = ElectricGuitar()
electric_guitar.play()
electric_guitar.play_louder()
