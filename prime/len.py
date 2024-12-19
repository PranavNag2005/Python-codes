# Take input from the user
input_str = input("Enter a string: ")

# Calculate the length of the string
length = len(input_str)

# Check if the length is even or odd
if length % 2 == 0:
    # Length is even, print the first half
    first_half = input_str[:length // 2]
    print("First half of the string:", first_half)
else:
    # Length is odd, remove the middle character
    middle_index = length // 2
    modified_str = input_str[:middle_index] + input_str[middle_index + 1:]
    print("String after removing the middle character:", modified_str)