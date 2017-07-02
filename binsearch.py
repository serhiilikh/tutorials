searched = 66
list1 = [1, 3, 5, 55, 66, 77, 160]
leftIndex = 0
rightIndex = len(list1)-1
middleIndex = int(rightIndex/2)
while list1[middleIndex]!=searched and rightIndex>leftIndex:
    if list1[middleIndex] < searched:
        print("middle become left", list1[middleIndex])
        print("right the same", list1[rightIndex])
        leftIndex=middleIndex + 1
    else:
        print("middle become right", list1[middleIndex])
        print("left the same", list1[leftIndex])
        rightIndex=middleIndex - 1
    middleIndex = int((leftIndex + rightIndex) / 2)
print("result: ",list1[middleIndex])
