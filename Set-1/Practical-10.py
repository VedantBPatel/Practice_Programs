def base_conversion():
    number=input("Enter a number: \n")
    from_base=int(input("From Base:"))
    to_base=int(input("To Base:"))

    decimal=int(number,from_base)
    result=""
    chars="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while decimal>0:
        result=chars[decimal%to_base]+result
        decimal //=16
        print(f"Converted number is {result or '0'}")
base_conversion()
