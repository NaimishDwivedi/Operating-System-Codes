# FCFS -> First Come First Serve

n = int(input("Enter the number of processes: "))

wt = []
bt = []
tat = []
avwt = 0
avtat = 0

print("Enter the process burst time : ")
for i in range (n):
    print("P[",i,"]")
    bt.append(int(input()))

wt.append(0) # first process has waiting time 0 always in FCFS
for i in range (1 , n):
    wt.append(0) # if all process come simultaneously
    for j in range (i):
        wt[i] += bt[j]

for i in range (n):
    tat.append(wt[i] + bt [i])
    avwt += wt[i]
    avtat += tat[i]

print("Average waiting time is : ", avwt/n)
print("Average waiting time is : ", avtat/n)
