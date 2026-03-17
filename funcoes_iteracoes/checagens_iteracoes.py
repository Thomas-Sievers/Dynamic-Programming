nums = [10, 20, 0, 30]

print("any > 25 ?", any(x > 25 for x in nums))
print("all > 0 ?", any(x > 0 for x in nums))

print("Sum: ", sum(nums))
print("Min: ", min(nums))
print("Max: ", max(nums))