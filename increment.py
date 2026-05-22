# Function to round numbers to the nearest 10

def round_to_10(numbers):

    # Start at index 0
    i = 0

    # Keep looping while i is smaller than the length of the list
    while i < len(numbers):

        # Round the number to the nearest 10
        # Divide by 10, round it, then multiply by 10 again
        numbers[i] = round(numbers[i] / 10) * 10

        # Move to the next position in the list
        i = i + 1

    # Return the new updated list
    return numbers


# Example
print(round_to_10([12, 25, 67, 81]))


# Function that increments numbers less than 40 by 2

def change_numbers(numbers):

    # Variable to count numbers less than 50
    count = 0

    # Start at index 0
    i = 0

    # Loop through the list using a while loop
    while i < len(numbers):

        # Check if the number is less than 40
        if numbers[i] < 40:

            # Add 2 to the number
            numbers[i] = numbers[i] + 2

        # Check if the new number is less than 50
        if numbers[i] < 50:

            # Increase the count by 1
            count = count + 1

        # Move to the next number
        i = i + 1

    # Return a tuple:
    # (new list, count)
    return (numbers, count)


# Example
print(change_numbers([10, 25, 40, 55]))