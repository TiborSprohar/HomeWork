stevilka1 = int(input("Vnesi prvo številko: "))


operation = input("Izberi računsko operacijo, ki je lahko +, -, * ali /: ")

stevilka2 = int(input("Vnesi drugo številko: "))

if operation == "+":
    print(stevilka1 + stevilka2)

elif operation == "-":
    print(stevilka1 - stevilka2)

elif operation =="*":
    print(stevilka1 * stevilka2)

elif operation == "/":
    print(stevilka1 / stevilka2)
