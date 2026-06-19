def example2(nums):
    results = [1 for _ in range(len(nums))]

    for i, num1 in enumerate(nums):
        for num2 in nums:
            if num1 == num2:
                continue

            results[i] += num2

    return results

# O(n²)