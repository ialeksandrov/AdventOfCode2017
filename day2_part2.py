def main(inp):
    res = 0
    for i in range(len(inp)):
        nums = inp[i].rstrip('\n').split('\t')
        nums = [int(i) for i in nums]
        nums = sorted(nums, reverse=True)
        for x in range(len(nums)):
            for y in range(len(nums) - 1 - x):
                if nums[x] % nums[y + 1 + x] == 0:
                    res += nums[x] // nums[y + 1 + x]
                    break

    print(res)

with open("day2_data.txt", "r") as inputfile:
    main(inputfile.readlines())