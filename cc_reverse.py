def reverse(string):
    reverse_str = ''
    str_arr = list(string)
    while len(str_arr) > 0:
        reverse_str += str_arr.pop()
    return reverse_str


name = input("What is your name? ")
print("Your name reversed is:", reverse(name))