def removeDuplicates(nums):
    pos = 1
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
            if count > 2:
                continue
        else:
            count = 1
        nums[pos] = nums[i]
        pos += 1
    print(nums[:pos])
    return pos


removeDuplicates([1, 1, 1, 2, 2, 3])
removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3])
