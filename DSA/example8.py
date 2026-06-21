def example8(strings):
    for i, string in enumerate(strings): #n
        digits = 0

        for char in string: #k
            if char in [str(i) for i in range(0, 10)]:
                digit += 1

        if digits >= len(string) / 2:
            string[i] = sorted(strings[i]) # klo₂(k)

    return strings

# n(klog₂(k))