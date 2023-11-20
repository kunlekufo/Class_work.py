def hello_name(user_name):
    greeting = "hello_" + user_name + "!"
    print(greeting)

hello_name("John")

def first_odds():
    for number in range(1, 101, 2):
        print(number)

# Call the function to see the output
first_odds()

def max_num_in_list(a_list):
    # Check if the list is not empty
    if not a_list:
        return "The list is empty."

    # Initialize the maximum number with the first element of the list
    max_num = a_list[0]

    # Iterate through the list to find the maximum number
    for num in a_list:
        if num > max_num:
            max_num = num

    return max_num

# Example usage:
my_list = [3, 7, 1, 15, 9, 5]
result = max_num_in_list(my_list)
print(f"The maximum number in the list is: {result}")

def is_leap_year(a_year):
    # Leap year conditions
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
        return True
    else:
        return False

# Example usage:
year_to_check = 2020
result = is_leap_year(year_to_check)
print(f"{year_to_check} is a leap year: {result}")

def is_consecutive(a_list):
    # Check if the list is empty
    if not a_list:
        return False

    # Find the minimum and maximum values in the list
    min_val = min(a_list)
    max_val = max(a_list)

    # Check if the difference between max and min values is equal to the length of the list
    return max_val - min_val == len(a_list) - 1 and len(set(a_list)) == len(a_list)

# Example usage:
consecutive_list = [2, 3, 4, 5, 6, 7]
non_consecutive_list = [1, 2, 4, 5]

print(is_consecutive(consecutive_list))  # Should print True
print(is_consecutive(non_consecutive_list))  # Should print False





