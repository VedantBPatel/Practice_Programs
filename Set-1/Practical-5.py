def is_leapyear():
    year=int(input("Enter a year: \n"))
    if (year%4==0 and year%100!=0)or(year%400==0):
        print(f"{year} is a leap year.\n")
    else:
        print(f"{year} is not a leap yaer.\n")
is_leapyear()