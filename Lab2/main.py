import numpy as np
import time
import timeit
import statistics

def naiveMxMult(a, b):
    n = len(a)
    res = np.zeros((n, n), dtype=int)
    for i in range(len(a)):  # rows in a
        for j in range(len(b[0])):  # cols in b
            for k in range(len(b)):  # rows in b
                res[i][j] += ((a[i][k]) * (b[k][j]))
    return res

def MxAdd(a, b):
    n = len(a)
    res = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            res[i][j] = a[i][j] + b[i][j]
    return res

def MxSub(a, b):
    n = len(a)
    res = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            res[i][j] = a[i][j] - b[i][j]
    return res


def dncMxMultiply(a, b):
    if len(a) == 2:
        return naiveMxMult(a, b)
    mid = len(a) // 2
    a1 = a[:mid, :mid]  # Top-left corner, a
    a2 = a[:mid, mid:]  # Top-right corner, a
    a3 = a[mid:, :mid]  # Bottom-left corner, a
    a4 = a[mid:, mid:]  # Bottom-right corner, a

    b1 = b[:mid, :mid]  # Top-left corner, b
    b2 = b[:mid, mid:]  # Top-right corner, b
    b3 = b[mid:, :mid]  # Bottom-left corner, b
    b4 = b[mid:, mid:]  # Bottom-right corner, b

    c1 = (MxAdd(dncMxMultiply(a1, b1), dncMxMultiply(a2, b3)))
    c2 = (MxAdd(dncMxMultiply(a1, b2), dncMxMultiply(a2, b4)))
    c3 = (MxAdd(dncMxMultiply(a3, b1), dncMxMultiply(a4, b3)))
    c4 = (MxAdd(dncMxMultiply(a3, b2), dncMxMultiply(a4, b4)))

    res = np.zeros((len(a), len(a)), dtype=int)
    for i in range(len(c1)):
        for j in range(len(c1)):
            res[i][j] = c1[i][j]
            res[i][j + len(c1)] = c2[i][j]
            res[i + len(c1)][j] = c3[i][j]
            res[i + len(c1)][j + len(c1)] = c4[i][j]
 #   res[:mid, :mid] = c1
 #   res[:mid, mid:] = c2
 #   res[mid:, :mid] = c3
 #   res[mid:, mid:] = c4
    return res


def strassen_multiply(A, B):
    n = len(A)
    if n == 2:
        return naiveMxMult(A, B)
    mid = n // 2

    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    M1 = strassen_multiply(MxAdd(A11, A22), MxAdd(B11, B22))
    M2 = strassen_multiply(MxAdd(A21, A22), B11)
    M3 = strassen_multiply(A11, MxSub(B12, B22))
    M4 = strassen_multiply(A22, MxSub(B21, B11))
    M5 = strassen_multiply(MxAdd(A11, A12), B22)
    M6 = strassen_multiply(MxSub(A21, A11), MxAdd(B11, B12))
    M7 = strassen_multiply(MxSub(A12, A22), MxAdd(B21, B22))

    C11 = MxAdd(MxSub(MxAdd(M1, M4), M5), M7)
    C12 = MxAdd(M3, M5)
    C21 = MxAdd(M2, M4)
    C22 = MxAdd(MxAdd(MxSub(M1, M2), M3), M6)


    res = np.zeros((n, n), dtype=int)
    res[:mid, :mid] = C11
    res[:mid, mid:] = C12
    res[mid:, :mid] = C21
    res[mid:, mid:] = C22
    return res

def runTests(repeats):
    archivedMatrices = []
    results = []
    for i in range(1, 11):
        dim = 2**i
        naive_times = []
        dnc_times = []
        strassens_times = []
        for j in range(repeats):
            a = np.random.randint(100, size=(dim, dim))
            b = np.random.randint(100, size=(dim, dim))
            t1 = timeit.timeit(lambda: naiveMxMult(a, b), number=1)
            naive_times.append(t1)
            t2 = timeit.timeit(lambda: dncMxMultiply(a, b), number=1)
            dnc_times.append(t2)
            t3 = timeit.timeit(lambda: strassen_multiply(a, b), number=1)
            strassens_times.append(t3)
            archivedMatrices.append(a)
            archivedMatrices.append(b)
        print("Array size:", 2**i, "*", 2**i)
        print("Naive", statistics.mean(naive_times), statistics.stdev(naive_times))
        print("DNC", statistics.mean(dnc_times), statistics.stdev(dnc_times))
        print("Strassens", statistics.mean(strassens_times), statistics.stdev(strassens_times))
        results.append([naive_times, dnc_times, strassens_times])
    print(results)


def main():
    runTests(10)
if __name__ == "__main__":
    main()
