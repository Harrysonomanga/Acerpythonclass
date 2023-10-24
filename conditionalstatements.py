temperature = 56

if temperature > 37:
    print("It is too hot!")
else:
    print("It is cold")

# Python program that returns the largest number among three numbers
num1 = 45
num2 = 34
num3 = 67
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "Is the largest number ")
else:
    print(num3, "Is the greatest number")

Age = 66
if Age >= 18:
    print("Congratulations! You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# Assignment
# Python program that checks whether a year is a leap year or not
year = int(input("Enter the year:"))

if year % 4 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year")


# Python program that checks whether alphabet is a vowel or a consonant
alphabet = "e"
if len(alphabet) == 1:
    vowels = 'aeiou'
    if alphabet in vowels:
        print(alphabet, "is a vowel.")
    else:
        print(alphabet, "is a consonant.")


