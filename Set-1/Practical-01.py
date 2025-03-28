def convert_temperature():
    choice = input("Convert to (C)elcius or (F)arenhite?\n").strip().lower()
    
    if choice == "c":
        f= float(input("Enter the temperature in Farenhite: \n"))
        print(f"{f}F is {(f-32)*5/9 :.2f}) C")
    elif choice == "f":
        c=float(input("Enter the temperature in Celcius: \n"))
        print(f"{c}C is {(c*9/5) +32: .2f} F")
    else:
        print("Invalid choic, Please enter 'C' or 'F'. ")

convert_temperature()

