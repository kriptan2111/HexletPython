def join_numbers_from_range(start, end):
    numbers = range(start, end+1)
    return ''.join(map(str, numbers))

start = 1
end = 10
result = join_numbers_from_range(start, end)
print(result)


"""
start= 3
finish=5

def multiply_numbers_from_range(start, finish):
    i = start
    multiply = 1

    while i <= finish:
        multiply *= i

        i += 1
    return multiply

print(multiply_numbers_from_range(start, finish))
"""