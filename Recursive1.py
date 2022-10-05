def CountUp(N):
    if N == 0:
        return
    CountUp(N-1)
    print(N, end=" ")


def CountDown(N):
    if N == 0:
        return
    print(N, end=" ")
    CountDown(N-1)


def SUM(N):
    if N == 0:
        return 0
    result = N + SUM(N-1)
    return result


def POW(N, x):
    if x == 0:
        return 1
    return N * POW(N, x-1)


def FIBO(N):
    if N == 1:
        return 0
    elif N == 2 or N == 3:
        return 1
    return FIBO(N-1) + FIBO(N-2)


def FIND_MAX(LIST):
    if len(LIST) == 1:
        return LIST[0]
    MAX = FIND_MAX(LIST[1::])
    return MAX if MAX > LIST[0] else LIST[0]


def FIND_MIN(LIST):
    if len(LIST) == 1:
        return LIST[0]
    MIN = FIND_MIN(LIST[1::])
    return MIN if MIN < LIST[0] else LIST[0]


def Special_SUM(N):
    if N == 0:
        return 0
    result = N + Special_SUM(N-1)
    print(result, end=" ")
    return result


def FORLOOP(FROM, TO, i=None):
    if i == None:
        i = FROM
    if i == TO:
        return
    print(f"FROM {FROM} TO {TO} : i = {i}")
    if FROM < TO:
        FORLOOP(FROM, TO, i+1)
    else:
        FORLOOP(FROM, TO, i-1)


def WHILELOOP(N):
    if N > 13:
        return
    print("Hello")
    WHILELOOP(N+2)


LIST = [4, 8, -7, -5, 3, 1, 2]
CountUp(5)
CountDown(5)
print()
print(SUM(5))
print(POW(5, 2))
print(FIBO(5))
print(FIND_MAX(LIST))
print(FIND_MIN(LIST))
print("{", end=" ")
Special_SUM(5)
print("} #Special_SUM")
FORLOOP(0, 5)
WHILELOOP(5)
