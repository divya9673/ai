n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

for i in range(n):

    small = i

    for j in range(i + 1, n):

        if arr[j] < arr[small]:
            small = j

    arr[i], arr[small] = arr[small], arr[i]

print("Sorted List:")
print(arr)



#1. Start the program.
#2. Input the number of elements.
#3. Read all elements into the array.
#4. Assume the current element as the smallest element.
#5. Compare it with the remaining unsorted elements.
#6. Find the smallest element in the unsorted part of the array.
#7. Swap the smallest element with the current element.
#8. Repeat the process for all positions in the array.
#9. Display the sorted list.
#10. End the program.
