def part(arr):
    part_terms = ["Partridge", "PearTree", "Chat", "Dan", "Toblerone", "Lynn", "AlphaPapa", "Nomad"]
    count = 0
    # compare two items in list
    for term in arr:
        if term in part_terms:
    # if in part_terms, add 1 to count
            count += 1
    if count > 0:
        return "Mine's a Pint" + (count * "!")
    else:
        return "Lynn, I've pierced my foot on a spike!!"