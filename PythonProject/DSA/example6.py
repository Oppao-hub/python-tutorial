def example6(lst, search_lst):
    max_value = max(lst)

    for value in search_lst:
        if max_value == value:
            return True
        
    return False

# O(n + m)