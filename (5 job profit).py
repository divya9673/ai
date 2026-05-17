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




#Enter number of jobs:
#4
#
#Enter job name: J1
#Enter deadline: 2
#Enter profit: 100
#
#Enter job name: J2
#Enter deadline: 1
#Enter profit: 50
#
#Enter job name: J3
#Enter deadline: 2
#Enter profit: 10
#
#Enter job name: J4
#Enter deadline: 1
#Enter profit: 20
#
#Selected Jobs:
#['J1', 'J2']
#
#Total Profit: 150



#Algorithm
#
#1. Start the program.
#2. Input the number of jobs.
#3. Read each job name, deadline, and profit.
#4. Store all jobs in a list.
#5. Sort the jobs in decreasing order of profit.
#6. Find the maximum deadline among all jobs.
#7. Create empty time slots up to the maximum deadline.
#8. Select the job with the highest profit first.
#9. Place the job in the latest available slot before its deadline.
#10. If a slot is available, assign the job and add its profit.
#11. Repeat for all jobs.
#12. Display the selected jobs and total profit.
#13. End the program.
#
#⸻
#
#Why it is a Greedy Approach
#
#This code implements the Job Sequencing with Deadline problem using a Greedy Algorithm because:
#
#* At every step, it selects the job with the highest profit first.
#* It makes the locally optimal choice to maximize profit.
#* Once a job is assigned to a slot, the decision is not changed.
#* The algorithm greedily schedules jobs to get the maximum total profit within deadlines.
