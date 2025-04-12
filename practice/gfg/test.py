def first_repeating_element(arr):
    seen = set()
    first_index = -1

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] in seen:
            first_index = i
        else:
            seen.add(arr[i])
    print(seen)
    if first_index == -1:
        return -1  # No repeating element found
    else:
        return first_index + 1  # Convert to 1-based indexing

# Example usage:
arr = [10, 5, 3, 4, 3, 5, 6]
print(first_repeating_element(arr))