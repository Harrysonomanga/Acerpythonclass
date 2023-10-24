# User defined functions
def greeting():
    print("Hello world!")


greeting()


def sum():
    print(6 + 7)


sum()


def details():
    print("Harry", "web dev")


details()


# parameters and arguments
def student(firstname, course, age):
    print(firstname, course, age)


student(firstname="Harrison", course="web development", age=22)
student(firstname="Risper", course="Computer Science", age=22)
student(firstname="Denver", course="Android", age=24)
student(firstname="Davin", course="Data Science", age=27)


# Built-in Library functions
y = max(40, 13, 56, 79, 45)
print(y)

x = min(89, 90, 6, 67, 54)
print(x)