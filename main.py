#question number one#
def find_largest_number(numbers):
    if len(numbers) == 0:
        return None  # Return None if the list is empty
    largest_number = numbers[0]  # Assume the first number is the largest
    for number in numbers:
        if number > largest_number:
            largest_number = number  # Update the largest number if a larger number is found
    return largest_number
# Example usage
numbers = [12, 43, 7, 99, 22, 36]
largest = find_largest_number(numbers)

#Question number two#
print("The largest number is:", largest)
def print_primes(n):
    # A prime number is greater than 1 and only divisible by 1 and itself
    for num in range(2, n+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
# Example usage
print_primes(20)

#Question number three#
def reverse_number(number):
    reversed_number = 0

    while number != 0:
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number //= 10
