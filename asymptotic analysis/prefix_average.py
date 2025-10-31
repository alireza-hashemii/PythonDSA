# 1- consecutive averages - O(n^2)
def prefix_average1(S):
    n = len(S)
    A = [0] * n

    for i in range(n):
        total = 0
        for j in range(i + 1):
            total += S[j]
        A[i] = total / (i + 1)

    return A



# 1- consecutive averages. An alternative: O(N)
def prefix_average1(S):
    n = len(S)
    A = [0] * n

    for i in range(n):
        total += S[i]
        A[i] = total / (i + 1)
        
    return A




