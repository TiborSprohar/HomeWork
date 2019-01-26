
print("Hello, this program converts kilometers into miles!!")

while True:

    km = int(input("Enter number of kilometers: "))
    convert = km * 0.621371192
    print("It is  " + str(convert) + " miles")
    answer = input("Would You like to do another conversion (Use: Yes/No)? ")
    answer = answer.lower()
    if answer == "no":
        print("Thank You and Goodbye")
        break










