def lowest_to_highest(arr):
    return sorted(arr)

def highest_to_lowest(arr):
    return sorted(arr, reverse=True)

# Get user input and convert to integers
input_arr = list(map(int, input("Enter numbers separated by space: ").split()))

print(f"The lowest to highest sorted array is: {lowest_to_highest(input_arr)}")
print(f"The highest to lowest sorted array is: {highest_to_lowest(input_arr)}")
