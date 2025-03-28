def count_words(filepath):
    try:
        with open(filepath,'r')as f:
            words=f.read().split()
            print(len(words))
    except FileNotFoundError:
        print("File not Found, Please enter valid file path.")
count_words("Practice_Programs/Set-2/textfile.txt")
"""
If our file is so deep inside the folders.... start giving path after we enter our main directory like here my main directory was starting from programming so in the path of the desired file i gave path till the file excluding programming.
"""