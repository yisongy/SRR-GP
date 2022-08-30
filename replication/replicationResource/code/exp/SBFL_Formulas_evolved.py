def EFF10_83(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]
        ranking[i, 2] = pow(line[4], line[1]) + line[2] - 1

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def EFF11_82(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]
        ranking[i, 2] = abs(line[1] + line[2] - 1)

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def EFF8_16(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]
        ranking[i, 2] = abs(2 * line[1] + line[3] - line[4] / line[1])

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def EFF5_98(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]
        ranking[i, 2] = (line[1] - line[4]) + line[3] * line[1]

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def EFF3_149(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]
        fz = pow(line[4], line[4])
        fm = line[4] - line[2] - line[3] - 1
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def EFF7_34(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]
        ranking[i, 2] = 2 * line[3] + (line[1] + line[3] - line[4]) * line[1]

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def EFF8_137(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]
        ranking[i, 2] = pow(line[3], line[1] + line[3] - line[4] + line[2] + 1)

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def EFF11_42(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]
        ranking[i, 2] = pow(line[1], line[1] + line[3]) - line[4]

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def EFF11_8(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]
        ranking[i, 2] = line[1] * (line[4] + line[1] + 1) - line[4]

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def EFF4_38(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]
        ranking[i, 2] = -line[1] * (pow(line[2], 2) + line[3] * line[1])

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

