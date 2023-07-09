# Write a function that returns both the minimum and maximum number of the given list/array.


lst = [4, 3, 1, 2, 6, 5]


def min_max(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[::len(sorted_lst)-1]

