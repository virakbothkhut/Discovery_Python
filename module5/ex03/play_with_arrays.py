original_array = [2, 8, 9, 48, 8, 22, -12, 2]
modified_array = set(x + 2 for x in original_array if x >5)
print(original_array)
print(modified_array)