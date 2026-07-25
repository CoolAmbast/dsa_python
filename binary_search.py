# O(log n) time complexity
def binary_search(list,target):
    first = 0
    last = len(list) - 1
    while first <= last:
        mid= (first+last)//2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid + 1
        else:
            last = mid -1
    return None

def verify(index):
    if index is not None:
        print("Target at index: ",index)
    else:
        print("Target not found")
        
num = [1,2,3,4,5,6,7,8,9,10] #needs to be sorted before searching otherwise it will return None even if the target is present in list 
res = binary_search(num,10)
verify(res)