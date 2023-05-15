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
print("The largest number is:", largest)
