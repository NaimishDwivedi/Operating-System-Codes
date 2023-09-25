# Round Robin implementation using python
def findWaitingTime(p, n ,bt, wt, q): # q = quantum
    rem_bt = bt.copy()
    t = 0
    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False

                if rem_bt[i] > q:
                    t += q
                    rem_bt[i] -= q

                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if done:
            break

def findTurnAroundTime(p, n,bt, wt, tat):
    for i in range (n):
        tat[i] = bt[i] + wt[i]

def findAvgTime(p, n, bt, q):
    wt = [0]  * n
    tat = [0] * n
    avwt = 0
    avtat = 0

    findWaitingTime(p, n ,bt,wt, q)
    findTurnAroundTime(p, n,bt, wt, tat)

    for i in range (n):
        avwt += wt[i]
        avtat += tat[i]

    print("Average waiting time is : ", avwt/n)
    print("Average waiting time is : ", avtat/n)

if __name__ == "__main__":
    p = [1,2,3]
    n = len(p)
    bt = [10,5,8]
    q = 2
    findAvgTime(p, n , bt ,q)
