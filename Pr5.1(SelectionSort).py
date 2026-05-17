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