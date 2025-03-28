def calculate_average():
    numbers = list(map(float, input("Enter numbers separated by space: \n").split()))
    average = sum(numbers)/len(numbers)
    print(f"Average of Numbers of Given list is: {average:.2f}")
calculate_average()
