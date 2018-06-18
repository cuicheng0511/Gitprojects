# encoding:utf-8

# 升序排列

def aesc(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key



# 降序排列
def desc(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] < key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


# 线性查找
def liner_search(A, v):
    for i in range(0, len(A)):
        if A[i] == v:
            return i
        else:
            return -1


# 二进制加法
def bin_add(A, B):
    flag = 0
    n1 = len(A)
    n2 = len(B)
    if n1 >= n2:
        C = [0] * (n1 + 1)
        C = [int(i) for i in C]
        temp = '0'*(n1 - n2)
        B = temp + B
        n = n1
    else:
        C = [0] * (n2 + 1)
        C = [int(i) for i in C]
        temp = '0'*(n1 - n2)
        A = temp + A
        n = n2
    for i in range(n - 1, -1, -1):
        key = int(A[i]) + int(B[i]) + flag
        if key >= 2:
           C[i + 1] = key - 2
           flag = 1
        else:
            C[i + 1] = key
            flag = 0
    C[0] = flag
    return C


