def example4(nested_list):
    total = 0

    for inner_list in nested_list: # H
        for num in inner_list: #W
            total += num

        for num in inner_list: #W
            total += num

        for num in inner_list: #W
            total += num
        
    return total

# O(HW)

#H = height W = width