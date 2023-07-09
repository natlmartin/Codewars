arr = { 6, 2, 1, 8, 10 }


def sum_array(arr):
    if not arr:
        return 0
    else:
        return sum(sorted(arr)[1:-1])

sum_array(arr)