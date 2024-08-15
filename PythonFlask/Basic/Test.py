lst = []
nums = input("Enter numbers separated by spaces: ").split()
target = int(input("Enter the target number: "))

nums = [int(num) for num in nums]

found = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            lst.append((i, j))
            found = True
            break
    if found:
        break

if lst:
    print(lst[0])
else:
    print("No pairs found that add up to the target.")