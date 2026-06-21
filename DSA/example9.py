def example9(dict1, dict2): # n, m
    keys1 = sorted(dict1.keys()) # n log₂(n)
    keys2 = sorted(dict1.keys()) # m log₂(m)

    process = keys1 + keys2 # n + m
    results = set()

    while len(process) > 0: # (n + m) k
        element = process.pop(0) #n + m
        results.append(element)

        if len(element) == 1:
            continue

        process.append(element[:-1])

    return results

# O(nlog₂(n) + mlog₂(m) + (n + m)k)