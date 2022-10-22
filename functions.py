def Fib(n):
    import numpy as np
    fib = np.array([0, 1, 1])
    nfib = np.array([0, 1, 2])
    for i in range(2, n):
        fib = np.append(fib, [fib[-1] + fib[-2]])
        nfib = np.append(nfib, [nfib[-1] + 1])
    return(fib)

def Sort(a):
    for i in range(len(a)):
         for j in range(len(a)-1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return(a)

def Calc(a, b, s):
    if s == '+':
        return a+b
    if s == '-':
        return a-b
    if s == '*':
        return a*b
    if s == '/':
        return a/b