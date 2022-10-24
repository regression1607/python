def binary_search(a, x):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


a = [1, 2, 3, 4, 5]
s=binary_search(a,6)
if s!=-1:
    print("Number found and Index Number is ", s)
else:
    print("Number not found")