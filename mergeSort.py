import random

def mergeSort(arr):
    """
    Simple Merge Sort Algorithm. Uses Recursion
    Sorts an array with an O(n * log(n)) time complexity
    Divide and Conquer Algorithm

    Args:
      arr (required) - An unsorted array which you want to Sort

    Returns:
      Nothing - Sorts the array in place
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)
    merge(arr, left, right)

def merge(arr, left, right):
  """
  Used with Merge algorithm

  Args:
    arr (required) - The unsorted array you want to sort
    left (required) - The left side of the array. Values to the left of the "mid" index
    right (required) - The right side of the array. Values to the right of the "mid" index

  Returns:
    Nothing - Sorts array in place
  """
  l_index = 0
  r_index = 0

  while l_index < len(left) and r_index < len(right):
      if left[l_index] <= right[r_index]:
        arr[l_index + r_index] = left[l_index]
        l_index += 1
      else:
        arr[l_index + r_index] = right[r_index]
        r_index += 1

  arr[l_index + r_index:] = left[l_index:] + right[r_index:]


def mergeSortReturnsVal(arr):
    """
    Simple Merge Sort Algorithm. Uses Recursion.
    Sorts an array with O(n * log(n)) time complexity
    

    Args:
      arr (required) - The unsorted array you want to sort
    
    Returns:
      A Sorted array
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSortReturnsVal(left)
    right = mergeSortReturnsVal(right)
    return mergeReturnsVal(left, right)

def mergeReturnsVal(left, right):
    """
    Used with mergeSortReturnsVal function.

    Args:
      left (required) - Takes in the values to the left of the mid value within the array
      right (required) - Takes in the values to the right of the mid value within the array

    Returns:
      A sorted array. (After all Recursions completed)
    """
    l_index = 0
    r_index = 0
    result = []
    none_values = []

    while l_index < len(left) and r_index < len(right):
        try:
            if left[l_index] <= right[r_index]:
                result.append(left[l_index])
                l_index += 1
            else:
                result.append(right[r_index])
                r_index += 1
        except TypeError:
            if left[l_index] == None:
                none_values.append(left[l_index])
                l_index += 1
            else:
                none_values.append(right[r_index])
                r_index += 1
    result.extend(left[l_index:])
    result.extend(right[r_index:])
    result.extend(none_values)
    return result


data = [100,23,4342,123,5343,5342,5353,1,435,756,435,89,7,8,43,1,32]
data = mergeSortReturnsVal(data)
print('Sorted Array in Ascending Order:')
print(data)