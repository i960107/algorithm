def removeElement(nums, val):
    pos = 0
    # index 0 부터 확인해야함. val일 경우 대체되어야함.
    for i in range(len(nums)):
        if nums[i] != val:
            nums[pos] = nums[i]
            pos += 1
    print(nums[:pos])
    return pos

removeElement(nums=[3, 2, 2, 3], val=3)
