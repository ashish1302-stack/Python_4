# Exercise 1
Students = ['Ashish', 'Rahul', 'Anjali', 'Meera']
print(f"The length of the list: {len(Students)}")
'''
The len() function is used to return the number of items (length)
in an object, such as a string, list, tuple,
dictionary, or other iterable objects.
'''


# Exercise 2
Name1 = input("Enter your name: ")
print(f"Hello, {Name1}!")


# Exercise 3
def find_maximum(numbers):
    if not numbers:  # Check for an empty list
        return None
    max_value = numbers[0]  # Assume the first number is the maximum
    for num in numbers:
        if num > max_value:  # Compare each number with the current maximum
            max_value = num
    return max_value

numbers = [12, 23, 34, 45, 56, 67, 78, 89]
max_num = find_maximum(numbers)
print(f"The max number is: {max_num}")


# Exercise 4
x = 15  # Global variable

def my_function():
    x = 8  # Local variable
    print("Local x inside the function:", x)

my_function()
print("Global x outside the function:", x)
'''
Here when we call the function (my_function), it reads the x (x=8) inside the block,
not the global variable x.
'''

# Exercise 5
def calculate_area(length, width=6):
    area = length * width
    return area

area1 = calculate_area(8, 4)
print(f"Area with length: 8 and width: 4: {area1}")

area2 = calculate_area(7)
print(f"Area with length: 7: {area2}")
