#O(n) time complexity
def linear_search(list,target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target at index: ",index)
    else:
        print("Target not found")

num = [1,2,3,4,5,6,7,8,9,10] #can be sorted or unsorted, doesn't matter!
#res = linear_search(num, 12)
#verify(res)
res = linear_search(num, 6)
verify(res)
