import pandas as pd
import json

def mergeSort(arr, key):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left, key)
    right = mergeSort(right, key)
    return merge(left, right, key)

def merge(left, right, key):
    l_index = 0
    r_index = 0
    result = []
    none_values = []

    while l_index < len(left) and r_index < len(right):
        try:
            if left[l_index][key] <= right[r_index][key]:
                result.append(left[l_index])
                l_index += 1
            else:
                result.append(right[r_index])
                r_index += 1
        except TypeError:
            if left[l_index][key] == None:
                none_values.append(left[l_index])
                l_index += 1
            else:
                none_values.append(right[r_index])
                r_index += 1

    result.extend(left[l_index:])
    result.extend(right[r_index:])
    result.extend(none_values)
    return result

def binarySearch(arr, key, target):
    low = 0
    high = len(arr) - 1
    target_formatted = "".join(target.lower().split())

    while low <= high:
        mid = (low + high) // 2
        mid_value = "".join(str(arr[mid][key]).lower().split())

        if target_formatted in mid_value:
            return mid
        elif mid_value < target_formatted:
            low = mid + 1
        elif mid_value > target_formatted:
            high = mid - 1
    return None

contents = pd.read_csv('100kbooks.csv')
books = json.loads(contents.to_json(orient='records'))

catagory = input("Would you like to search using ISBN, Title, Author, Year, Publisher - ").lower()
if catagory.startswith("i"):
    print("You have chosen catagory - ISBN")
    catagory = "ISBN"
elif catagory.startswith("t"):
    print("You have chosen catagory - Title")
    catagory = "Title"
elif catagory.startswith("a"):
    print("You have chosen catagory - Author")
    catagory = "Author"
elif catagory.startswith("y"):
    print("You have chosen catagory - Year")
    catagory = "Year"
elif catagory.startswith("p"):
    print("You have chosen catagory - Publisher")
    catagory = "Publisher"
else:
    print("Catagory not found!")
    catagory = None

if catagory is not None:
    books = mergeSort(books, catagory)
    search = input("Enter your search query - ")
    res = binarySearch(books, catagory, search)

    if res:
        print("Result Found")
        print(f"Book\nISBN: {books[res]["ISBN"]}\nTitle: {books[res]["Title"]}")
        print(f"Author: {books[res]["Author"]}\nYear: {books[res]["Year"]}\nPublisher: {books[res]["Publisher"]}\n")