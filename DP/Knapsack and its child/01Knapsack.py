# study it before taking the code this is very tricky one
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

#memoizing it now:
t = [[-1 for x in range(W+1)]for y in range(n+1)]


# writing the recursion code to find the Optimal solution
def knapsack(W, wt, val, n):
    # write the base condition for Knapsack
    if W == 0 or n == 0:
        return 0
    #using the table thing
    if t[n][W] != -1:
        return t[n][W]

    #choice based approach

    elif wt[n-1] > W:
        t[n][W] = knapsack(W, wt, val, n-1)  # store it first then return
        return t[n][W]
    else:
        t[n][W] = max(val[n-1]+knapsack(W-wt[n-1], wt, val, n-1),
                      knapsack(W, wt, val, n-1))
        return t[n][W]


print(knapsack(W, wt, val, n))



