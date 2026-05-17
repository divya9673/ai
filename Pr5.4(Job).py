n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):
    name = input("Enter job name: ")
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter profit: "))

    jobs.append([name, deadline, profit])

jobs.sort(key=lambda x: x[2], reverse=True)

max_deadline = 0

for i in jobs:
    if i[1] > max_deadline:
        max_deadline = i[1]

slot = [0] * max_deadline
result = []

profit = 0

for job in jobs:

    for j in range(job[1] - 1, -1, -1):

        if slot[j] == 0:
            slot[j] = 1
            result.append(job[0])
            profit += job[2]
            break

print("Selected Jobs:")
print(result)

print("Total Profit:", profit)