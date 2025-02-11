# Quicksort Algorithm in Python

## Introduction
Quicksort is a highly efficient, divide-and-conquer sorting algorithm that works by selecting a "pivot" element and partitioning the array into elements less than, equal to, and greater than the pivot. The process is then recursively applied to the partitions until the entire list is sorted.

## Implementation
Below is a Python implementation of Quicksort:

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]    # Elements less than pivot
    middle = [x for x in arr if x == pivot] # Elements equal to pivot
    right = [x for x in arr if x > pivot]   # Elements greater than pivot
    return quicksort(left) + middle + quicksort(right)  # Recursive call
```

## How Quicksort Works

### **1. Base Case (Stopping Condition)**
- If the list has **one or zero elements**, it is already sorted, so we return it immediately.

```python
if len(arr) <= 1:
    return arr
```

### **2. Choosing a Pivot**
- The pivot is chosen as the middle element of the list:

```python
pivot = arr[len(arr) // 2]
```

### **3. Partitioning the Array**
- The list is divided into three parts:
  - `left`: Elements **less than** the pivot.
  - `middle`: Elements **equal to** the pivot.
  - `right`: Elements **greater than** the pivot.

```python
left = [x for x in arr if x < pivot]    # Create a list of elements < pivot
middle = [x for x in arr if x == pivot] # Create a list of elements = pivot
right = [x for x in arr if x > pivot]   # Create a list of elements > pivot
```

### **4. Recursively Sorting the Partitions**
- The algorithm calls itself on the `left` and `right` partitions.
- The sorted partitions are then combined with the `middle` elements.

```python
return quicksort(left) + middle + quicksort(right)
```

## Example Walkthrough
### Input:
```python
arr = [3, 10, 2, 8, 6, 1]
print(quicksort(arr))
```
### Steps:
1. **Choose Pivot**: `pivot = 8`
2. **Partitioning**:
   - `left = [3, 2, 6, 1]`
   - `middle = [8]`
   - `right = [10]`
3. **Recursive Sorting**:
   - Sorting `[3, 2, 6, 1]` (pivot = `6`) → `[1, 2, 3, 6]`
   - Sorting `[10]` (already sorted)
4. **Combining**:
   - `[1, 2, 3, 6] + [8] + [10] = [1, 2, 3, 6, 8, 10]`

## Time Complexity
| Case       | Complexity |
|------------|------------|
| Best Case  | O(n log n) |
| Average Case | O(n log n) |
| Worst Case  | O(n²) (when pivot selection is poor) |

## Advantages & Disadvantages
### ✅ Advantages
- **Fast**: O(n log n) on average.
- **In-place Variant Exists**: Although this implementation uses extra space, an in-place version can be implemented.

### ❌ Disadvantages
- Worst-case O(n²) if the pivot is chosen poorly (e.g., always selecting the largest or smallest element).
- Uses extra space in this particular implementation due to list comprehensions.

## Conclusion
Quicksort is one of the most commonly used sorting algorithms due to its efficiency and simplicity. It leverages recursion and partitioning to efficiently sort an array in **O(n log n)** time on average. However, choosing a good pivot is crucial for performance.