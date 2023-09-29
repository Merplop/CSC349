import numpy as np

def FindMaxLinear(a):
    n = len(a)
    largest = a[0]
    for i in range(n):
        if largest < a[i]:
            largest = a[i]
    return largest

def FindMaxLinearWithCount(a):
    n = len(a)
    largest = a[0]
    count = 0
    for i in range(n):
        if largest < a[i]:
            count += 1
            largest = a[i]
        elif largest > a[i]:
            count += 1
    return [largest, count]

def FindMaxDNC(a,i,j):
    if i == j:
        return a[i]
    k = int(i+(j-i)/2)
    l = FindMaxDNC(a, i, k)
    m = FindMaxDNC(a, k+1, j)
    if l > m:
        return l
    return m

def FindMaxDNCWithCount(a,i,j):
    if i == j:
        return [a[i], 0]
    k = int(i+(j-i)/2)
    l = FindMaxDNCWithCount(a, i, k)
    m = FindMaxDNCWithCount(a, k+1, j)
    if l[0] > m[0]:
        l[1] += 1
        return l
    m[1] += 1
    return m

def FindSecondLinear(a):
    largest = a[0]
    compared = []
    for n in a:
        if n > largest:
            compared.clear()
            compared.append(largest)
            largest = n
        elif n < largest:
            compared.append(n)
    print("[for internal debugging] Values compared to largest: ", compared)
    return FindMaxLinear(compared)

def FindSecondLinearWithCount(a):
    largest = a[0]
    compared = []
    count = 0
    for n in a:
        if n > largest:
            compared.clear()
            compared.append(largest)
            largest = n
            count+=1
        elif n < largest:       # not else to account for duplicate value edge-case
            compared.append(n)
            count+=1
    print("[for internal debugging] Values compared to largest: ", compared)
    return FindMaxLinear(compared), count

def FindSecondDNC(a):
    n = len(a)
    compared = FindSecondDNCWithComps(a, 0, n-1, n)
    print("[for internal debugging] Return value of FindSecondDNCWithComps: ", compared)
    compared2 = FindMaxDNC(compared, 2, compared[0])
    return compared2

def FindSecondDNCWithComps(a, i, j, n):
    if i == j:
        compared = [0]*n
        compared[0] = 1
        compared[1] = a[i]
        return compared
    mid = int(i+(j-i)/2)
    compared1 = FindSecondDNCWithComps(a, i, mid, n)
    compared2 = FindSecondDNCWithComps(a, mid+1, j, n)
    if compared1[1] > compared2[1]:
        k = compared1[0]+1
        compared1[0] = k
        compared1[k] = compared2[1]
        return compared1
    else:
        if compared1[1] == compared2[1]:        # if duplicate, ignore. Kind of sketchy solution but it seems to work
            return compared2
        k = compared2[0]+1
        compared2[0] = k
        compared2[k] = compared1[1]
        return compared2

def FindSecondDNCWithCount(a,i,j):
    n = len(a)
    compared = FindSecondDNCWithComps(a, 0, n - 1, n)
    print("[for internal debugging] Return value of FindSecondDNCWithComps: ", compared)
    compared2 = FindMaxDNC(compared, 2, compared[0])
    return [compared2, n-1]
