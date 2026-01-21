while True:
    zahl1 = (input('   '))


    operator = (input("  "))

    zahl2 = (input('   '))



    if operator == "+":
        result = (float(zahl1)) + (float(zahl2))
        print (f"{zahl1} + {zahl2} = {result}")

    elif operator == "-":
        result = (float(zahl1)) - (float(zahl2))
        print (f"{zahl1} - {zahl2} = {result}")

    elif operator == "*":
        result = (float(zahl1)) * (float(zahl2))
        print (f"{zahl1} * {zahl2} = {result}")

    elif operator == "/":
        result = (float(zahl1)) / (float(zahl2))
        print (f"{zahl1} / {zahl2} = {result}")

    else:
         print("fehler")


