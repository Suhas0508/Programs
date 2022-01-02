# Binary search is the search technique that works efficiently on sorted lists. Hence, 
# to search an element into some list using the binary search technique, we must ensure that the list is sorted.

# Binary search follows the divide and conquer approach 
# in which the list is divided into two halves, and the item is compared with the middle element of the list.
# If the match is found then, the location of the middle element is returned. 
# Otherwise, we search into either of the halves depending upon the result produced through the match.


# Seaching Array Element using Binary search algorithm

arr = [1,2,3,4,5,6,7,8,9]
print(f"Element list = {arr}")

min = 0
max = 8
flag = 0

num = int(input("Enter element : "))

while min<=max:
    mid = int((min+max)/2)
    
    if arr[mid]==num:
        flag = 1
        break
    
    if(arr[mid]<num):
        min = mid+1
    else:
        max = mid-1
        
if flag == 1:
    print(f"{num} found at {mid}")
else:
    print(f"{num} Not Found..!!")
