def Longest(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]  # Сгенерировать матрицу 0, чтобы облегчить последующие вычисления, на один столбец больше, чем длина строки
    mmax = 0  # Длина самого длинного совпадения
    p = 0  # Самое длинное совпадение соответствует последнему биту в s1
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]: # Если равно, добавить существующую общую подстроку
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > mmax:
                    mmax = m[i + 1][j + 1]
                    p = i + 1
    return s1[p - mmax:p], mmax