def fib(num):
    if num == 0:
        print(0)
    elif num == 1 or num == 2: 
        print(1)
    else:
        num_arr = [0,1,1]
        while len(num_arr) <= num:
            length = len(num_arr)
            new_num = num_arr[length - 2] + num_arr[length - 1]
            num_arr.append(new_num)
        print(num_arr.pop())
print('Fibonacci')
print()
num = int(input('Enter a Number: '))
fib(num) 