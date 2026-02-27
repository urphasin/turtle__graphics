import turtle

t = "hello"


student = {
    "name": "Otito",
    "age": 18,
    "major": "Math"
}
print(student.get("names"))

def print_address(**something):
  for values in something.values():
    print(values, end=", ")
  print()


print_address(
  street= "1375 Village Loop Rd",
  city= "Ogden",
  zipcode= "84403",
  state="Utah"
)

my_list = ["banana", "mangos", "pinefruit"]

print(help(list))
print("\n\n")
print(dir(my_list))


friends = {
  "brady": 2,
  "desmond": 4,
  "krishna": 4
}

family = {
  "mom": 1,
  "amarachi": 2, 
  "ebube": 4,
  "otito": 3, 
}

courses = {
  "cs1300": "hard",
  "cs1400": "hard",
  "web1400": "hard",
  "math1050": "hard",
  "math1060": "hard"
}
