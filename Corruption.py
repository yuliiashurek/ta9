from numpy import random


def corruption(N, P):
    sum = 0
    percent = (100 - P) / 100
    list = []
    for i in range(0, N):
        G = random.randint(0, 10000)
        list.append(G)
        sum += list[i]

    temp = 0
    firstMin = 10001
    secondMin = 10001
    firstMinIndex = 0
    secondMinIndex = 0

    while len(list) > 1:
        for i in range(0, len(list)):
            if list[i] < firstMin:
                secondMin = firstMin
                secondMinIndex = firstMinIndex
                firstMin = list[i]
                firstMinIndex = i
            elif list[i] < secondMin:
                secondMin = list[i]
                secondMinIndex = i
        temp = (firstMin + secondMin) * percent
        list[firstMinIndex]= temp
        list.remove(list[secondMinIndex])
        firstMin = 10_000 * N
        secondMin = 10_000 * N

    return list[0]
