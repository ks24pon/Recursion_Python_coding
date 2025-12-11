from math import sqrt

def perfectNumberList(n):
    if n < 6:
        return "none"
    
    count = []

    for i in range(6, n + 1):
        sumDivisors = 1
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                sumDivisors += j
                if j != i // j:
                    sumDivisors += i // j

        if sumDivisors == i:
            count.append(str(i))

    return "-".join(count) if count else "none"