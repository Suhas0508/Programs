# Linear search (known as sequential search) is an algorithm 
# for finding a target value within a list. 
# It sequentially checks each element of the list for the target value 
# until a match is found or until all the elements have been searched.


# Find givem element is present in array or not 


arr = [7,5,8,4,2,3,9]
print(f"Element list = {arr}")
flag=0
num = int(input("Enter Element to search : "))

for i in range(len(arr)):
    if(arr[i] == num):
        flag = 1
        break
if(flag == 1):
    print(f"{num} Found at {i} position")
else:
    print(f"{num} not found..!!")
