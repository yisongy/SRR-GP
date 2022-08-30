from exp.getExeResult import *
from exp.getSpectrum import *
from numpy import *
import itertools
import copy

def loadDataSet(fileName):
    table = xlrd.open_workbook(fileName).sheets()[0]
    row = table.nrows
    col = table.ncols
    datamatrix = np.zeros((row, col))
    for x in range(col):
        cols = np.matrix(table.col_values(x))
        datamatrix[:, x] = cols
    datamatrix = mat(datamatrix)
    return datamatrix

def Euclidean(x, y):
    return np.sqrt(np.sum(np.square(x-y)))

# calculate Euclidean distance of ranking
def getEuclideanCsv(NewGroup, failed):
    path = str(os.getcwd()) + str('/EuclideanCsv')
    if not os.path.exists(path):
        os.mkdir(path)

    for formula in NewGroup:

        dataSet = loadDataSet('rank_mat/' + formula + '_ranking.csv')

        m = shape(dataSet)[1] - 1
        data = {}
        i = 1
        for case in failed:
            data['t' + str(case)] = dataSet[:, i].flatten().A[0]
            i += 1

        distance_dict = {}
        for i in range(0, m):
            for j in range(i + 1, m):
                dis = Euclidean(data['t' + str(failed[i])], data['t' + str(failed[j])])
                distance_dict['t' + str(failed[i]) + '_' + 't' + str(failed[j])] = dis

        new_distance_dict = copy.deepcopy(distance_dict)
        for i in range(0, m):
            new_distance_dict['t' + str(failed[i]) + '_' + 't' + str(failed[i])] = 0
            for j in range(i + 1, m):
                new_distance_dict['t' + str(failed[j]) + '_' + 't' + str(failed[i])] = \
                    distance_dict['t' + str(failed[i]) + '_' + 't' + str(failed[j])]

        f = xlsxwriter.Workbook('EuclideanCsv/' + formula + '_distance.csv')
        sheet1 = f.add_worksheet(u'sheet1')
        dict_row = 0
        for k, v in new_distance_dict.items():
            sheet1.write(dict_row, 0, k)
            sheet1.write(dict_row, 1, v)
            dict_row += 1
        f.close()
        print(formula + '.csv Euclidean distance has been calculated')

# Clustering for one formula
def kmedoidsCluster(failed, formula, k):
    m = len(failed)

    read_distanceDict = {}
    distance_list = []
    table = xlrd.open_workbook('EuclideanCsv/' + formula + '_distance.csv').sheets()[0]
    row = table.nrows
    for key in range(row):
        read_distanceDict[table.row_values(key)[0]] = table.row_values(key)[1]
        if key < m * (m - 1) / 2:
            distance_list.append(table.row_values(key)[1])

    centroids = ['144', '348']

    if len(centroids) != k:
        if len(centroids) > k:
            file = open('clusterAssment/' + formula + ' (medoids_over).txt', 'w')
            file.write(str(len(centroids)))
            file.close()
            return -1
        elif len(centroids) < k:
            file = open('clusterAssment/' + formula + ' (medoids_under).txt', 'w')
            file.write(str(len(centroids)))
            file.close()
            return -1

    print('centroids = ' + str(centroids))

    clusterAssment = mat(zeros((m, 2)))
    medoidsChanged_sign = True
    z = 1
    while medoidsChanged_sign:
        medoidsChanged_sign = False
        for i in range(m):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = read_distanceDict['t' + str(failed[i]) + '_t' + str(centroids[j])]

                if distJI < minDist:
                    minDist = distJI
                    minIndex = j

            clusterAssment[i, :] = failed[i], minIndex
        medoidsChanged_num = 0
        currentChanged = 0
        for cent in range(k):
            ptsInClust = np.array(failed)[nonzero(clusterAssment[:, 1].A == cent)[0]]

            sumMin = 0
            for otherPoint in ptsInClust:
                sumMin += read_distanceDict['t' + str(centroids[cent]) + '_t' + str(otherPoint)]

            for newMedoids_candidate in ptsInClust:
                sumReplace = 0
                for otherPoint in ptsInClust:
                    sumReplace += read_distanceDict['t' + str(newMedoids_candidate) + '_t' + str(otherPoint)]

                if sumReplace < sumMin:
                    sumMin = sumReplace
                    centroids[cent] = str(newMedoids_candidate)
                    medoidsChanged_sign = True
                    currentChanged = 1
            medoidsChanged_num += currentChanged
            currentChanged = 0
        z += 1

    f = xlsxwriter.Workbook('clusterAssment/' + formula + '.xls')
    sheet1 = f.add_worksheet(u'sheet1')
    [h, l] = clusterAssment.shape
    for i in range(h):
        for j in range(l):
            sheet1.write(i, j, clusterAssment[i, j])
    f.close()
    return clusterAssment

# The project dir
home_dir = "../dataset/Example/flex-A03-A12"

# Go to project dir
os.chdir(home_dir)

# Get results of testcases
Label0, LabelA, LabelB = getLabel()
failed, succ = getfailedAndsucc(Label0)

# Get spectrum
exeFormula(failed, succ)

# Calculate distance
getEuclideanCsv(['OTH11_gp19'], failed)

# Make folder for clustering results
path = str(os.getcwd()) + str('/clusterAssment')
if not os.path.exists(path):
    os.mkdir(path)

# Clustering
kmedoidsCluster(failed, 'OTH11_gp19', 2)