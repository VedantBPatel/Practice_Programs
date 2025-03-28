def is_palindrome():
    text = input("Enter a string: \n").strip().lower()
    if text == text[::-1]:
        print(f"{text} is a palindrome \n")
    else:
        print(f"{text} is not a palindorme \n")
is_palindrome()