def sum_of_evens():
    total = 0
    for number in range(1, 101):
        if number % 2 == 0:
            total += number
    return total

result = sum_of_evens()
print(f"The sum of all even numbers from 1 to 100 is: {result}")
