# Given an array of integers, remove the smallest value.
# Do not mutate the original array/list.
# If there are multiple elements with the same value, remove the one with a lower index.
# If you get an empty array/list, return an empty array/list.
# Don't change the order of the elements that are left.

# numbers = [5, 3, 2, 1, 4]
numbers = [2]
# numbers = [347, 212, 338, 55, 134, 398, 323, 82, 144]


def remove_smallest(numbers):
    # [:] - copies whole array
    a = numbers[:]
    # if array contains elements
    if a:
        a.remove(min(a))
    print(a)


remove_smallest(numbers)

# if len(numbers) > 1:
#         sorted_numbers = sorted(numbers)
#         smallest_number = sorted_numbers[0]
#         for number in numbers:
#             if number == smallest_number:
#                 numbers.remove(number)
#                 break
#         return numbers
#     else:
#         return []

## Explanation of array - index slicing
# del arr # Deletes the array itself
# del arr[:]  # Deletes all the elements in the array
# del arr[2]  # Deletes the second element in the array
# del arr[1:]  # etc..