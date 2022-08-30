from exp.dependencies import *
import os
programList = ['flex', 'grep', 'gzip', 'sed']

RQ1_variables = "a list of all SBFL formulas"

RQ2_variables = ['2bug', '3bug', '4bug', '5bug']

RQ3_variables = ['TypeA', 'TypeP', 'TypeH']

metricList = ['FMI', 'JC', 'PR', 'RR']

# The dir which contains all faulty versions
allVersionDir = "/home/exp/"

def getMetrics(test = False):
    if test == True:
        programList = ['flex']

        RQ1_variables = ['OTH11_gp19']

        RQ2_variables = ['2bug']

        RQ3_variables = ['TypeA']

    for programName in programList:
        for faultNumber in RQ2_variables:
            for typeName in RQ3_variables:

                for metricName in metricList:
                    if faultNumber[0] == '2':
                        permutationNumber = 2
                    elif faultNumber[0] == '3':
                        permutationNumber = 6
                    elif faultNumber[0] == '4':
                        permutationNumber = 24
                    elif faultNumber[0] == '5':
                        permutationNumber = 120

                    if metricName == 'RR':
                        getTableRow = 1
                    if metricName == 'PR':
                        getTableRow = 2
                    if metricName == 'JC':
                        getTableRow = 3
                    if metricName == 'FMI':
                        getTableRow = 4


                    tableRowNum = 20 * permutationNumber

                    dataMat = np.zeros((tableRowNum, len(RQ1_variables)))

                    path = allVersionDir + programName + "/" + faultNumber + "/" + typeName
                    if test == True:
                        path = "../dataset/Example"
                    file = os.listdir(path)
                    file.sort()
                    content = []
                    for versionName in file:
                            content.append(versionName)

                    row_sign = 0
                    for distribution in content:
                        subPath = path + '/' + str(distribution) + '/clusterAssment/metric'

                        col_sign = 0
                        for formula in RQ1_variables:
                            if os.path.exists(subPath + '/' + formula + str('_metric.xls')):
                                table = xlrd.open_workbook(subPath + '/' + formula + str('_metric.xls')).sheets()[0]

                                metric_data = np.matrix(table.row_values(getTableRow))
                                metric_data = metric_data[0, 1:]
                                dataMat[row_sign: row_sign + permutationNumber, col_sign] = metric_data.T.flatten().A[0]

                            col_sign += 1
                        row_sign += permutationNumber

                    if not os.path.exists(path + '/data_sum'):
                        os.mkdir(path + '/data_sum')
                    f = xlsxwriter.Workbook(path + '/data_sum/' + programName + '-' + faultNumber[0] + typeName[-1] + \
                                            '-' + metricName + '.xls')
                    sheet1 = f.add_worksheet(u'sheet1')
                    [h, l] = dataMat.shape
                    for i in range(h):
                        for j in range(l):
                            sheet1.write(i, j, dataMat[i, j])
                    f.close()
                    if test == True:
                        break
