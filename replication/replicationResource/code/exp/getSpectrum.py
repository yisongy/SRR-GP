from exp.dependencies import *
from numpy import zeros
from numpy import mat
import os
def single(c, t, exline):
    NUS = 0; NUF = 0; NCS = 0; NCF = 0
    table = zeros((exline, 10))
    k = 0
    covf = open("traces/cov_t" + str(c))
    for line in covf:
        if line[0:9] != "        -":
            order = line[10:15]
            if t == 1:
                if line[0:9] == "    #####":
                    NUF += 1
                else:
                    NCF += 1
            else:
                if line[0:9] == "    #####":
                    NUS += 1
                else:
                    NCS += 1
            NC = NCF + NCS
            NS = NCS + NUS
            NU = NUS + NUF
            NF = NCF + NUF
            N = NC + NU

            table[k, :] = [order, NCS, NCF, NUS, NUF, NC, NS, NU, NF, N]
            NUS = 0; NUF = 0; NCS = 0; NCF = 0
            k += 1
    return table

def muti(failed, formula, succ_table_sum, exline):
    rank_mat = np.zeros((1 + len(failed), exline))
    k = 1

    covf = open("traces/cov_t" + str(1))
    num_array = []
    for line in covf:
        if line[0:9] != "        -":
            order = line[10:15]
            num_array.append(order)

    for num_array_index in range(exline):
        rank_mat[0, num_array_index] = num_array[num_array_index]

    for failed_number in failed:
        failed_table = single(failed_number, 1, exline)
        table_sum = failed_table + succ_table_sum

        table_sum = mat(table_sum)
        np.set_printoptions(suppress=True)

        ranking = globals()[formula](table_sum, exline)
        for i in range(1, exline):
            if ranking[i, 2] == ranking[i - 1, 2]:
                ranking[i, 0] = ranking[i - 1, 0]
            else:
                ranking[i, 0] = i + 1
                ranking = ranking[ranking[:, 1].argsort()]
                rank_mat[k, :] = ranking[:, 0]
        k += 1

    f = xlsxwriter.Workbook('rank_mat/' + str(formula) + '_ranking.csv')
    sheet1 = f.add_worksheet(u'sheet1')
    rank_mat_t = rank_mat.T
    [h, l] = rank_mat_t.shape
    for i in range(h):
        for j in range(l):
            sheet1.write(i, j, rank_mat_t[i, j])
    f.close()
    return rank_mat

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

def exeFormula(failed, succ):
    path = str(os.getcwd()) + str('/rank_mat')
    if not os.path.exists(path):
        os.mkdir(path)

    exline = 0
    covf = open("traces/cov_t" + str(1))
    for line in covf:
        if line[0:9] != "        -":
            exline += 1

    succ_table_sum = zeros((exline, 10))
    for succ_number in succ:
        succ_table = single(succ_number, 0, exline)
        succ_table_sum[:, 1:] += succ_table[:, 1:]

    rank_mat = muti(failed, 'OTH11_gp19', succ_table_sum, exline)
    print("processing raw coverage data into spectrum information, please wait...")
    print(rank_mat)
