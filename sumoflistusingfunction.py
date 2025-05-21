def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
nums = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    num = int(input("Enter element {}: ".format(i + 1)))
    nums.append(num)
result = calculate_sum(nums)
print("The sum of the result is", result)
