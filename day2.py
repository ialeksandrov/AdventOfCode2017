def main(inp):
    res = 0
    for i in range(len(inp)):
        nums = inp[i].rstrip('\n').split('\t')
        nums = [int(i) for i in nums]
        res += int(sorted(nums)[-1]) - int(sorted(nums)[0])

    print(res)

with open("day2_data.txt", "r") as inputfile:
    main(inputfile.readlines())