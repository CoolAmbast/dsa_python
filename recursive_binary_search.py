def recursive_binary_search(list,target):
    if len(list) == 0:
        return False
    else:
        mid = (len(list))//2
        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                return recursive_binary_search(list[mid+1:],target)
            else:
                return recursive_binary_search(list[:mid],target)

def verify(result):
    print("Target found: ", result)
    
num = [1,2,3,4,5,6,7,8,9,10]
res = recursive_binary_search(num, 9)
verify(res)

res = recursive_binary_search(num, 12)
verify(res)