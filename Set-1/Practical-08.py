def order_sorting():
    numbers = list(map(float, input("Enter numbers separated by space: \n").split()))
    order= input("Want to Sort in (a)scending or (d)escending order? \n").strip().lower()
    if order == 'a':
        print(sorted(numbers))
    elif order == 'd':
        print(sorted(numbers,reverse=True))
    else:
        print("Invalid instuction \n")
order_sorting()
