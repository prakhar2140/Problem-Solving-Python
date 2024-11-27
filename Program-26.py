# WAP to find out the second lowest element of the list 

arr = [5,12,13,15,10,56,89,22,6,57]

minValue = float('-inf')
secondMinValue = float('-inf')
print(minValue)

for i in range(1,len(arr)):
    if arr[i]>minValue:
        secondMinValue =minValue
        minValue = arr[i]
    elif arr[i] > secondMinValue and arr[i] != minValue:
        secondMinValue = arr[i]
print("Second smallest element is", secondMinValue)