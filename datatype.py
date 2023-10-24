# Data type

number = 25  # int
second = 56.78  # float
text = "Hello there"  # string
ispythoninteresting = True  # bool

#  store multiple values in a single variable
cars = ["Toyota", "Nissan", "VW", "Land Rover"]  # list ordered and changeable
fruits = ("Banana", "Oranges", "Apples")  # tuple ordered and unchangeable
countries = {"Kenya", "Uganda", "Tunisia", "Algeria"}  # set unordered and unchangeable
details = {
    "firstname": "Harrison",
    "Age": 22,
    "course": "web development",
    "nationality": "Kenya"
}  # Dictionary -  key-value pair

print(second)
print(text)
print(ispythoninteresting)
print(cars)
print(fruits)
print(countries)
print(details["course"])
print(details["Age"])

#  determine the data type
print(type(number))
print(type(details))

# Typecasting - converting one data type to another
print(float(number))
print(int(second))
