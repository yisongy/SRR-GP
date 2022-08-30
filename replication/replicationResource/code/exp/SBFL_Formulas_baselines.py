def ER1_naish1(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        if line[2] < line[8]:
            ranking[i, 2] = -1
        elif line[2] == line[8]:
            ranking[i, 2] = line[6] - line[1]

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER1_naish2(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = line[1]
        fm = line[6] + 1
        ranking[i, 2] = line[2] - (fz / fm)

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER2_jaccard(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        ranking[i, 2] = line[2] / (line[1] + line[8])

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER2_anderberg(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = line[2]
        fm = line[2] + (line[4] + line[1]) * 2
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER2_sorensendice(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = line[2] * 2
        fm = line[2] * 2 + line[4] + line[1]
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER2_dice(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = line[2] * 2
        fm = line[8] + line[1]
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER2_goodman(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = line[2] * 2 - line[4] - line[1]
        fm = line[2] * 2 + line[4] + line[1]
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER3_tarantula(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = line[2] / line[8]
        fm = (line[2] / line[8]) + (line[1] / line[6])
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER3_qe(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        ranking[i, 2] = line[2] / line[5]

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER3_cbi(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        a = line[2] / line[5]
        b = line[8] / line[9]
        ranking[i, 2] = a - b

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER4_wong2(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        ranking[i, 2] = line[2] - line[1]

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER4_hamann(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = line[2] + line[3] - line[4] - line[1]
        fm = line[9]
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER4_simplematching(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        ranking[i, 2] = (line[2] + line[3]) / line[9]

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER4_sokal(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = (line[2] + line[3]) * 2
        fm = (line[2] + line[3]) * 2 + line[4] + line[1]
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER4_rogers(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = line[2] + line[3]
        fm = line[2] + line[3] + (line[4] + line[1]) * 2
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER4_hamming(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        ranking[i, 2] = line[2] + line[3]

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER4_euclid(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        ranking[i, 2] = sqrt(line[2] + line[3])

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER5_wong1(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        ranking[i, 2] = line[2]

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER5_russel(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        ranking[i, 2] = line[2] / line[9]

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER5_binary(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        if line[2] < line[8]:
            ranking[i, 2] = 0
        elif line[2] == line[8]:
            ranking[i, 2] = 1

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER6_scott(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = line[2] * line[3] * 4 - line[4] * line[1] * 4 - pow((line[4] - line[1]), 2)
        fm = (line[2] * 2 + line[4] + line[1]) * (line[3] * 2 + line[4] + line[1])
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def ER6_rogot1(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        a = line[2] / (line[2] * 2 + line[4] + line[1])
        b = line[3] / (line[3] * 2 + line[4] + line[1])
        ranking[i, 2] = (a + b) / 2

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def OTH1_kulczynski2(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        a = line[2] / line[8]
        b = line[2] / line[5]
        ranking[i, 2] = (a + b) / 2

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def OTH2_ochiai(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = line[2]
        fm = sqrt(line[8] * line[5])
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def OTH3_m2(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = line[2]
        fm = line[2] + line[3] + (line[4] + line[1]) * 2
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def OTH4_ample2(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        ranking[i, 2] = (line[2] / line[8]) - (line[1] / line[6])

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def OTH5_wong3(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        if line[1] <= 2:
            h = line[1]
        elif 2 < line[1] <= 10:
            h = 2 + 0.1 * (line[1] - 2)
        elif line[1] > 10:
            h = 2.8 + 0.001 * (line[1] - 10)

        ranking[i, 2] = line[2] - h

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def OTH6_amean(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = line[2] * line[3] * 2 - line[4] * line[1] * 2
        fm = line[5] * line[7] + line[8] * line[6]
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def OTH7_cohen(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = line[2] * line[3] * 2 - line[4] * line[1] * 2
        fm = line[5] * line[6] + line[8] * line[7]
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def OTH8_fleiss(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        fz = line[2] * line[3] * 4 - line[4] * line[1] * 4 - pow((line[4] - line[1]), 2)
        fm = (line[2] * 2 + line[4] + line[1]) + (line[3] * 2 + line[4] + line[1])
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def OTH9_gp02(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        a = line[2] + math.sqrt(line[3])
        b = math.sqrt(line[1])
        ranking[i, 2] = 2 * a + b

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def OTH10_gp03(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        a = pow(line[2], 2) - math.sqrt(line[1])
        b = abs(a)
        ranking[i, 2] = math.sqrt(b)

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def OTH11_gp19(table_sum, exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        a = line[1] - line[2] + line[4] - line[3]
        b = math.sqrt(abs(a))
        ranking[i, 2] = line[2] * b

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def OTH12_crosstab(table_sum,exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]

        ECF = (line[5] * line[8]) / line[9]
        ECS = (line[5] * line[6]) / line[9]
        EUF = (line[7] * line[8]) / line[9]
        EUS = (line[7] * line[6]) / line[9]

        p1 = pow((line[2] - ECF), 2) / ECF
        p2 = pow((line[1] - ECS), 2) / ECS
        p3 = pow((line[4] - EUF), 2) / EUF
        p4 = pow((line[3] - EUS), 2) / EUS

        chisquare = p1 + p2 + p3 + p4

        fai = (line[2] / line[8]) / (line[1] / line[6])

        if fai > 1:
            ranking[i, 2] = chisquare
        elif fai == 1:
            ranking[i, 2] = 0
        elif fai < 1:
            ranking[i, 2] = -chisquare

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

def OTH13_dstar(table_sum,exline):
    ranking = zeros((exline, 3))
    i = 0
    for line in table_sum:
        line = mat(line).flatten().A[0]
        ranking[i, 1] = line[0]
        fz = pow(line[2], 2)
        fm = line[4] + line[1]
        ranking[i, 2] = fz / fm

        i += 1
    ranking = ranking[ranking[:, 2].argsort()[::-1]]
    for i in range(0, exline):
        ranking[i, 0] = i + 1
    return ranking

