test = ["He", "Hell", "Hello I am", "Help", "help", "Hey", "Overwatch", "Valorant"]

def binarySearch(arr, target):
    """
    Simple Binary Search Algorithm.
    Finds exact value

    Args:
        arr (required) - A Sorted array which you want to search through
        target (required) - A value which you want to search for

    Returns:
        The index of the item within the sorted list or none if value is not found
    """
    low = 0
    high = len(arr) - 1
    target = target.lower()

    while low <= high:
        mid = (low + high) // 2
        if arr[mid].lower() == target:
            return mid
        elif arr[mid].lower() < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


def binarySearchWithPrefix(arr, target):
    """
    Binary Search Algorithm which uses prefixes
    Finds a value which starts with the target Prefix, No spaces allowed

    Args:
        arr (required) - A Sorted array which you want to search through
        target (required) - A value which you want to search for

    Returns:
        The index of the item within the sorted list or none if value is not found
    """
    low = 0
    high = len(arr) - 1
    target = target.lower()
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid].lower().startswith(target):
            return mid
        elif arr[mid].lower() < target:
            low = mid + 1
        else:
            high = mid - 1  
    return None


def binSearchPrefixAndMultiple(arr, target):
    """
    Binary Search Algorithm looks for multiple values within the list
    Finds a value which starts with the target prefix, no spaces allowed

    Args:
        arr (required) - A Sorted array which you want to search through
        key (required) - The Catagory which you want to search through
        target (required) - A value which you want to search for

    Returns:
        A List of results which contains all the valid values found within the list
    """
    low = 0
    high = len(arr) - 1
    target = target.lower()
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid].lower().startswith(target):
            return findMultiple(arr, target, mid)
        elif arr[mid].lower() < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

def findMultiple(arr, target, mid):
    """
    findMultiple Function
    Takes in the mid value found through the binarySearch function and checks values +1 and -1 until prefix is not the same

    Args:
        arr (required) - A Sorted array whcih you want to search through
        key (required) - The catagory you want to search through
        target (required) - A value which you want to search for
        mid (required) - The index found through the binarySearch function

    Returns:
        A list of results found
    """
    left = mid - 1
    right = mid + 1
    found = [mid]

    while left >= 0 and arr[left].lower().startswith(target):
        found.append(left)
        left -= 1
    
    while right < len(arr) and arr[right].lower().startswith(target):
        found.append(right)
        right += 1
    return found


results = binSearchPrefixAndMultiple(test, "he")
for res in results:
    print(f"Result - {test[res]}")