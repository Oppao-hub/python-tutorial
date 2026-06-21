def example3(nums1, nums2):
    results = []

    for num in nums1:
        results.append(num)

    for i, num in enumerate(nums2):
        if i >= len(results):
            results.append(1)
        results[i] *= num
    
    return results

# O(n + m) 