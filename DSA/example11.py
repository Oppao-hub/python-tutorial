def example11(nums): #n
    sum_to_end = [] #n
    count = 0
    for i in range(len(nums)): #n
        num1 = nums[i]
        sum_to_end.append(0)
        for j in range(i + 1, len(nums)): #n
            num2 = nums[j]
            sum_to_end[i] += num2

            for _ in sum_to_end: #n
                count += 1
                print(count)

    return sum_to_end

ans = example11([1,2,3,4,5,6,7])
print(ans)

# O(n³)