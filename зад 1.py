def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

# Пример:
numbers = [3, 1, 9, 4, 7]
print("Python:", selection_sort_desc(numbers))  # [9, 7, 4, 3, 1]